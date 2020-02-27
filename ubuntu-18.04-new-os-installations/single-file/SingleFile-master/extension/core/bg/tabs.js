/*
 * Copyright 2010-2020 Gildas Lormeau
 * contact : gildas.lormeau <at> gmail.com
 * 
 * This file is part of SingleFile.
 *
 *   The code in this file is free software: you can redistribute it and/or 
 *   modify it under the terms of the GNU Affero General Public License 
 *   (GNU AGPL) as published by the Free Software Foundation, either version 3
 *   of the License, or (at your option) any later version.
 * 
 *   The code in this file is distributed in the hope that it will be useful, 
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of 
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero 
 *   General Public License for more details.
 *
 *   As additional permission under GNU AGPL version 3 section 7, you may 
 *   distribute UNMODIFIED VERSIONS OF THIS file without the copy of the GNU 
 *   AGPL normally required by section 4, provided you include this license 
 *   notice and a URL through which recipients can access the Corresponding 
 *   Source.
 */
/* global browser, singlefile */

singlefile.extension.core.bg.tabs = (() => {

	const pendingPrompts = new Map();

	browser.tabs.onCreated.addListener(tab => onTabCreated(tab));
	browser.tabs.onActivated.addListener(activeInfo => onTabActivated(activeInfo));
	browser.tabs.onRemoved.addListener(tabId => onTabRemoved(tabId));
	return {
		onMessage,
		get: async options => {
			const tabs = await browser.tabs.query(options);
			return tabs.sort((tab1, tab2) => tab1.index - tab2.index);
		},
		create: async createProperties => {
			const tab = await browser.tabs.create(createProperties);
			return new Promise((resolve, reject) => {
				browser.tabs.onUpdated.addListener(onTabUpdated);
				browser.tabs.onRemoved.addListener(onTabRemoved);
				function onTabUpdated(tabId, changeInfo) {
					if (tabId == tab.id && changeInfo.status == "complete") {
						resolve(tab);
						browser.tabs.onUpdated.removeListener(onTabUpdated);
						browser.tabs.onRemoved.removeListener(onTabRemoved);
					}
				}
				function onTabRemoved(tabId) {
					if (tabId == tab.id) {
						reject();
						browser.tabs.onRemoved.removeListener(onTabRemoved);
					}
				}
			});
		},
		sendMessage: (tabId, message, options) => browser.tabs.sendMessage(tabId, message, options),
		remove: tabId => browser.tabs.remove(tabId),
		promptValue: async promptMessage => {
			const tabs = await browser.tabs.query({ currentWindow: true, active: true });
			return new Promise(async (resolve, reject) => {
				const selectedTabId = tabs[0].id;
				browser.tabs.onRemoved.addListener(onTabRemoved);
				pendingPrompts.set(selectedTabId, { resolve, reject });
				browser.tabs.sendMessage(selectedTabId, { method: "common.promptValueRequest", promptMessage });

				function onTabRemoved(tabId) {
					if (tabId == selectedTabId) {
						pendingPrompts.delete(tabId);
						browser.tabs.onUpdated.removeListener(onTabRemoved);
						reject();
					}
				}
			});
		},
		extractAuthCode: authURL => {
			return new Promise((resolve, reject) => {
				let authTabId;
				browser.tabs.onUpdated.addListener(onTabUpdated);
				browser.tabs.onRemoved.addListener(onTabRemoved);

				function onTabUpdated(tabId, changeInfo) {
					if (changeInfo && changeInfo.url == authURL) {
						authTabId = tabId;
					}
					if (authTabId == tabId && changeInfo && changeInfo.title && changeInfo.title.startsWith("Success code=")) {
						browser.tabs.onUpdated.removeListener(onTabUpdated);
						browser.tabs.onUpdated.removeListener(onTabRemoved);
						resolve(changeInfo.title.substring(13, changeInfo.title.length - 49));
					}
				}

				function onTabRemoved(tabId) {
					if (tabId == authTabId) {
						browser.tabs.onUpdated.removeListener(onTabUpdated);
						browser.tabs.onUpdated.removeListener(onTabRemoved);
						reject();
					}
				}
			});
		},
		launchWebAuthFlow: async options => {
			const tab = await browser.tabs.create({ url: options.url, active: true });
			return new Promise((resolve, reject) => {
				browser.tabs.onRemoved.addListener(onTabRemoved);
				function onTabRemoved(tabId) {
					if (tabId == tab.id) {
						browser.tabs.onRemoved.removeListener(onTabRemoved);
						reject(new Error("code_required"));
					}
				}
			});
		}
	};

	async function onMessage(message, sender) {
		if (message.method.endsWith(".init")) {
			singlefile.extension.ui.bg.main.onInit(sender.tab);
			singlefile.extension.core.bg.business.onInit(sender.tab);
			singlefile.extension.core.bg.autosave.onInit(sender.tab);
			singlefile.extension.core.bg.editor.onInit(sender.tab);
		}
		if (message.method.endsWith(".promptValueResponse")) {
			const promptPromise = pendingPrompts.get(sender.tab.id);
			if (promptPromise) {
				promptPromise.resolve(message.value);
				pendingPrompts.delete(sender.tab.id);
			}
		}
		if (message.method.endsWith(".getOptions")) {
			return singlefile.extension.core.bg.config.getOptions(message.url);
		}
		if (message.method.endsWith(".activate")) {
			await browser.tabs.update(message.tabId, { active: true });
		}
	}

	function onTabCreated(tab) {
		singlefile.extension.ui.bg.main.onTabCreated(tab);
	}

	async function onTabActivated(activeInfo) {
		const tab = await browser.tabs.get(activeInfo.tabId);
		singlefile.extension.ui.bg.main.onTabActivated(tab, activeInfo);
	}

	function onTabRemoved(tabId) {
		singlefile.extension.core.bg.tabsData.onTabRemoved(tabId);
		singlefile.extension.core.bg.editor.onTabRemoved(tabId);
		singlefile.extension.core.bg.business.onTabRemoved(tabId);
	}

})();