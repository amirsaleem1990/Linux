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

/* global browser, singlefile, setTimeout */

singlefile.extension.core.bg.tabsData = (() => {

	let persistentData, temporaryData, cleanedUp;
	setTimeout(() => getPersistent().then(tabsData => persistentData = tabsData), 0);
	return {
		onMessage,
		onTabRemoved,
		getTemporary,
		get: getPersistent,
		set: setPersistent
	};

	async function onMessage(message) {
		if (message.method.endsWith(".get")) {
			return getPersistent();
		}
		if (message.method.endsWith(".set")) {
			return setPersistent(message.tabsData);
		}
	}

	async function onTabRemoved(tabId) {
		if (temporaryData) {
			delete temporaryData[tabId];
		}
		const tabsData = await getPersistent();
		delete tabsData[tabId];
		setPersistent(tabsData);
	}

	function getTemporary(desiredTabId) {
		if (!temporaryData) {
			temporaryData = {};
		}
		if (desiredTabId !== undefined && !temporaryData[desiredTabId]) {
			temporaryData[desiredTabId] = {};
		}
		return temporaryData;
	}

	async function getPersistent(desiredTabId) {
		if (!persistentData) {
			const config = await browser.storage.local.get();
			persistentData = config.tabsData || {};
		}
		cleanup();
		if (desiredTabId !== undefined && !persistentData[desiredTabId]) {
			persistentData[desiredTabId] = {};
		}
		return persistentData;
	}

	async function setPersistent(tabsData) {
		persistentData = tabsData;
		await browser.storage.local.set({ tabsData });
	}

	async function cleanup() {
		if (!cleanedUp && singlefile.extension.core.bg.tabs) {
			cleanedUp = true;
			const allTabs = await singlefile.extension.core.bg.tabs.get({ currentWindow: true, highlighted: true });
			Object.keys(persistentData).filter(key => {
				if (key != "autoSaveAll" && key != "autoSaveUnpinned" && key != "profileName") {
					return !allTabs.find(tab => tab.id == key);
				}
			}).forEach(tabId => delete persistentData[tabId]);
			await browser.storage.local.set({ tabsData: persistentData });
		}
	}

})();