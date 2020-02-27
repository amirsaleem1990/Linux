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

/* global singlefile, URL, Blob, woleet */

singlefile.extension.core.bg.autosave = (() => {

	return {
		onMessage,
		onMessageExternal,
		onInit,
		isEnabled,
		refreshTabs
	};

	async function onMessage(message, sender) {
		const ui = singlefile.extension.ui.bg.main;
		if (message.method.endsWith(".init")) {
			const [options, autoSaveEnabled] = await Promise.all([singlefile.extension.core.bg.config.getOptions(sender.tab.url, true), isEnabled(sender.tab)]);
			return { options, autoSaveEnabled };
		}
		if (message.method.endsWith(".save")) {
			const tabId = sender.tab.id;
			const options = await singlefile.extension.core.bg.config.getOptions(sender.tab.url, true);
			if (options.autoClose) {
				singlefile.extension.core.bg.tabs.remove(tabId);
			}
			ui.onStart(tabId, 1, true);
			await saveContent(message, sender.tab);
			ui.onEnd(tabId, true);
			return {};
		}
	}

	async function onMessageExternal(message, currentTab) {
		if (message.method == "enableAutoSave") {
			const tabsData = await singlefile.extension.core.bg.tabsData.get(currentTab.id);
			tabsData[currentTab.id].autoSave = message.enabled;
			await singlefile.extension.core.bg.tabsData.set(tabsData);
			singlefile.extension.ui.bg.main.refreshTab(currentTab);
		}
		if (message.method == "isAutoSaveEnabled") {
			return isEnabled(currentTab);
		}
	}

	async function onInit(tab) {
		const [options, autoSaveEnabled] = await Promise.all([singlefile.extension.core.bg.config.getOptions(tab.url, true), isEnabled(tab)]);
		if (options && ((options.autoSaveLoad || options.autoSaveLoadOrUnload) && autoSaveEnabled)) {
			singlefile.extension.core.bg.business.saveTabs([tab], { autoSave: true });
		}
	}

	async function isEnabled(tab) {
		const config = singlefile.extension.core.bg.config;
		if (tab) {
			const [tabsData, rule] = await Promise.all([singlefile.extension.core.bg.tabsData.get(), config.getRule(tab.url)]);
			return Boolean(tabsData.autoSaveAll ||
				(tabsData.autoSaveUnpinned && !tab.pinned) ||
				(tabsData[tab.id] && tabsData[tab.id].autoSave)) &&
				(!rule || rule.autoSaveProfile != config.DISABLED_PROFILE_NAME);
		}
	}

	async function refreshTabs() {
		const tabs = singlefile.extension.core.bg.tabs;
		const allTabs = (await singlefile.extension.core.bg.tabs.get({}));
		return Promise.all(allTabs.map(async tab => {
			const [options, autoSaveEnabled] = await Promise.all([singlefile.extension.core.bg.config.getOptions(tab.url, true), isEnabled(tab)]);
			try {
				await tabs.sendMessage(tab.id, { method: "content.init", autoSaveEnabled, options });
			} catch (error) {
				// ignored
			}
		}));
	}

	async function saveContent(message, tab) {
		const options = await singlefile.extension.core.bg.config.getOptions(tab.url, true);
		const tabId = tab.id;
		options.content = message.content;
		options.url = message.url;
		options.frames = message.frames;
		options.canvases = message.canvases;
		options.fonts = message.fonts;
		options.stylesheets = message.stylesheets;
		options.images = message.images;
		options.posters = message.posters;
		options.usedFonts = message.usedFonts;
		options.shadowRoots = message.shadowRoots;
		options.imports = message.imports;
		options.referrer = message.referrer;
		options.updatedResources = message.updatedResources;
		options.backgroundTab = true;
		options.autoSave = true;
		options.incognito = tab.incognito;
		options.tabId = tabId;
		options.tabIndex = tab.index;
		let pageData;
		try {
			pageData = await singlefile.extension.getPageData(options, null, null);
			if (options.includeInfobar) {
				await singlefile.common.ui.content.infobar.includeScript(pageData);
			}
			const blob = new Blob([pageData.content], { type: "text/html" });
			if (options.saveToGDrive) {
				await singlefile.extension.core.bg.downloads.uploadPage(message.taskId, pageData.filename, blob, options, {});
			} else {
				pageData.url = URL.createObjectURL(blob);
				await singlefile.extension.core.bg.downloads.downloadPage(pageData, options);
			}
			if (pageData.hash) {
				await woleet.anchor(pageData.hash);
			}
		} finally {
			singlefile.extension.core.bg.business.onSaveEnd(message.taskId);
			if (pageData && pageData.url) {
				URL.revokeObjectURL(pageData.url);
			}
		}
	}

})();