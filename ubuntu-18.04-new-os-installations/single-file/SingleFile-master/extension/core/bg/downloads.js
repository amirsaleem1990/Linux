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

/* global browser, singlefile, Blob, URL, document, GDrive, woleet */

singlefile.extension.core.bg.downloads = (() => {

	const partialContents = new Map();
	const MIMETYPE_HTML = "text/html";
	const STATE_DOWNLOAD_COMPLETE = "complete";
	const STATE_DOWNLOAD_INTERRUPTED = "interrupted";
	const STATE_ERROR_CANCELED_CHROMIUM = "USER_CANCELED";
	const ERROR_DOWNLOAD_CANCELED_GECKO = "canceled";
	const ERROR_CONFLICT_ACTION_GECKO = "conflictaction prompt not yet implemented";
	const ERROR_INCOGNITO_GECKO = "'incognito'";
	const ERROR_INCOGNITO_GECKO_ALT = "\"incognito\"";
	const ERROR_INVALID_FILENAME_GECKO = "illegal characters";
	const ERROR_INVALID_FILENAME_CHROMIUM = "invalid filename";
	const CLIENT_ID = "207618107333-bktohpfmdfnv5hfavi1ll18h74gqi27v.apps.googleusercontent.com";
	const SCOPES = ["https://www.googleapis.com/auth/drive.file"];

	const manifest = browser.runtime.getManifest();
	const requestPermissionIdentity = manifest.optional_permissions && manifest.optional_permissions.includes("identity");
	const gDrive = new GDrive(CLIENT_ID, SCOPES);
	return {
		onMessage,
		download,
		downloadPage,
		uploadPage
	};

	async function onMessage(message, sender) {
		if (message.method.endsWith(".download")) {
			return downloadTabPage(message, sender.tab);
		}
		if (message.method.endsWith(".disableGDrive")) {
			const authInfo = await singlefile.extension.core.bg.config.getAuthInfo();
			singlefile.extension.core.bg.config.removeAuthInfo();
			await gDrive.revokeAuthToken(authInfo && (authInfo.accessToken || authInfo.revokableAccessToken));
			return {};
		}
		if (message.method.endsWith(".end")) {
			if (message.hash) {
				await woleet.anchor(message.hash);
			}
			singlefile.extension.core.bg.business.onSaveEnd(message.taskId);
			return {};
		}
		if (message.method.endsWith(".getInfo")) {
			return singlefile.extension.core.bg.business.getTasksInfo();
		}
		if (message.method.endsWith(".cancel")) {
			singlefile.extension.core.bg.business.cancelTask(message.taskId);
			return {};
		}
		if (message.method.endsWith(".cancelAll")) {
			singlefile.extension.core.bg.business.cancelAllTasks();
			return {};
		}
		if (message.method.endsWith(".saveUrls")) {
			singlefile.extension.core.bg.business.saveUrls(message.urls);
			return {};
		}
	}

	async function downloadTabPage(message, tab) {
		let contents;
		if (message.truncated) {
			contents = partialContents.get(tab.id);
			if (!contents) {
				contents = [];
				partialContents.set(tab.id, contents);
			}
			contents.push(message.content);
			if (message.finished) {
				partialContents.delete(tab.id);
			}
		} else if (message.content) {
			contents = [message.content];
		}
		if (!message.truncated || message.finished) {
			if (message.openEditor) {
				singlefile.extension.ui.bg.main.onEdit(tab.id);
				await singlefile.extension.core.bg.editor.open({ tabIndex: tab.index + 1, filename: message.filename, content: contents.join("") }, {
					backgroundSave: message.backgroundSave,
					saveToClipboard: message.saveToClipboard,
					saveToGDrive: message.saveToGDrive,
					confirmFilename: message.confirmFilename,
					incognito: tab.incognito,
					filenameConflictAction: message.filenameConflictAction,
					filenameReplacementCharacter: message.filenameReplacementCharacter,
					compressHTML: message.compressHTML,
					bookmarkId: message.bookmarkId,
					replaceBookmarkURL: message.replaceBookmarkURL
				});
			} else {
				if (message.saveToClipboard) {
					message.content = contents.join("");
					saveToClipboard(message);
					singlefile.extension.ui.bg.main.onEnd(tab.id);
				} else {
					await downloadBlob(new Blob([contents], { type: MIMETYPE_HTML }), tab.id, tab.incognito, message);
				}
			}
		}
		return {};
	}

	async function downloadBlob(blob, tabId, incognito, message) {
		try {
			if (message.saveToGDrive) {
				await uploadPage(message.taskId, message.filename, blob, {
					forceWebAuthFlow: message.forceWebAuthFlow,
					extractAuthCode: message.extractAuthCode
				}, {
					onProgress: (offset, size) => singlefile.extension.ui.bg.main.onUploadProgress(tabId, offset, size)
				});
			} else {
				message.url = URL.createObjectURL(blob);
				await downloadPage(message, {
					confirmFilename: message.confirmFilename,
					incognito,
					filenameConflictAction: message.filenameConflictAction,
					filenameReplacementCharacter: message.filenameReplacementCharacter
				});
			}
			singlefile.extension.ui.bg.main.onEnd(tabId);
		} catch (error) {
			if (!error.message || error.message != "upload_cancelled") {
				console.error(error); // eslint-disable-line no-console
				singlefile.extension.ui.bg.main.onError(tabId);
			}
		} finally {
			if (message.url) {
				URL.revokeObjectURL(message.url);
			}
		}
	}

	async function getAuthInfo(authOptions, force) {
		let authInfo = await singlefile.extension.core.bg.config.getAuthInfo();
		const options = {
			interactive: true,
			auto: authOptions.extractAuthCode,
			forceWebAuthFlow: authOptions.forceWebAuthFlow,
			requestPermissionIdentity,
			launchWebAuthFlow: options => singlefile.extension.core.bg.tabs.launchWebAuthFlow(options),
			extractAuthCode: authURL => singlefile.extension.core.bg.tabs.extractAuthCode(authURL),
			promptAuthCode: () => singlefile.extension.core.bg.tabs.promptValue("Please enter the access code for Google Drive")
		};
		gDrive.setAuthInfo(authInfo, options);
		if (!authInfo || !authInfo.accessToken || force) {
			authInfo = await gDrive.auth(options);
			if (authInfo) {
				await singlefile.extension.core.bg.config.setAuthInfo(authInfo);
			} else {
				await singlefile.extension.core.bg.config.removeAuthInfo();
			}
		}
		return authInfo;
	}

	async function uploadPage(taskId, filename, blob, authOptions, uploadOptions) {
		try {
			await getAuthInfo(authOptions);
			const taskInfo = singlefile.extension.core.bg.business.getTaskInfo(taskId);
			if (taskInfo && !taskInfo.cancelled) {
				const uploadInfo = await gDrive.upload(filename, blob, uploadOptions);
				singlefile.extension.core.bg.business.setCancelCallback(taskId, uploadInfo.cancelUpload);
				return await uploadInfo.uploadPromise;
			}
		}
		catch (error) {
			if (error.message == "invalid_token") {
				let authInfo;
				try {
					authInfo = await gDrive.refreshAuthToken();
				} catch (error) {
					if (error.message == "unknown_token") {
						authInfo = await getAuthInfo(authOptions, true);
					} else {
						throw error;
					}
				}
				if (authInfo) {
					await singlefile.extension.core.bg.config.setAuthInfo(authInfo);
				} else {
					await singlefile.extension.core.bg.config.removeAuthInfo();
				}
				await uploadPage(taskId, filename, blob, authOptions, uploadOptions);
			} else {
				throw error;
			}
		}
	}

	async function downloadPage(pageData, options) {
		const downloadInfo = {
			url: pageData.url,
			saveAs: options.confirmFilename,
			filename: pageData.filename,
			conflictAction: options.filenameConflictAction
		};
		if (options.incognito) {
			downloadInfo.incognito = true;
		}
		const downloadData = await download(downloadInfo, options.filenameReplacementCharacter);
		if (downloadData.filename && pageData.bookmarkId && pageData.replaceBookmarkURL) {
			await singlefile.extension.core.bg.bookmarks.update(pageData.bookmarkId, { url: downloadData.filename });
		}
	}

	async function download(downloadInfo, replacementCharacter) {
		let downloadId;
		try {
			downloadId = await browser.downloads.download(downloadInfo);
		} catch (error) {
			if (error.message) {
				const errorMessage = error.message.toLowerCase();
				const invalidFilename = errorMessage.includes(ERROR_INVALID_FILENAME_GECKO) || errorMessage.includes(ERROR_INVALID_FILENAME_CHROMIUM);
				if (invalidFilename && downloadInfo.filename.startsWith(".")) {
					downloadInfo.filename = replacementCharacter + downloadInfo.filename;
					return download(downloadInfo, replacementCharacter);
				} else if (invalidFilename && downloadInfo.filename.includes(",")) {
					downloadInfo.filename = downloadInfo.filename.replace(/,/g, replacementCharacter);
					return download(downloadInfo, replacementCharacter);
				} else if (invalidFilename && !downloadInfo.filename.match(/^[\x00-\x7F]+$/)) { // eslint-disable-line  no-control-regex
					downloadInfo.filename = downloadInfo.filename.replace(/[^\x00-\x7F]+/g, replacementCharacter); // eslint-disable-line  no-control-regex
					return download(downloadInfo, replacementCharacter);
				} else if ((errorMessage.includes(ERROR_INCOGNITO_GECKO) || errorMessage.includes(ERROR_INCOGNITO_GECKO_ALT)) && downloadInfo.incognito) {
					delete downloadInfo.incognito;
					return download(downloadInfo, replacementCharacter);
				} else if (errorMessage == ERROR_CONFLICT_ACTION_GECKO && downloadInfo.conflictAction) {
					delete downloadInfo.conflictAction;
					return download(downloadInfo, replacementCharacter);
				} else if (errorMessage.includes(ERROR_DOWNLOAD_CANCELED_GECKO)) {
					return {};
				} else {
					throw error;
				}
			} else {
				throw error;
			}
		}
		return new Promise((resolve, reject) => {
			browser.downloads.onChanged.addListener(onChanged);

			function onChanged(event) {
				if (event.id == downloadId && event.state) {
					if (event.state.current == STATE_DOWNLOAD_COMPLETE) {
						browser.downloads.search({ id: downloadId })
							.then(downloadItems => resolve({ filename: downloadItems[0] && downloadItems[0].filename }))
							.catch(() => resolve({}));
						browser.downloads.onChanged.removeListener(onChanged);
					}
					if (event.state.current == STATE_DOWNLOAD_INTERRUPTED) {
						if (event.error && event.error.current == STATE_ERROR_CANCELED_CHROMIUM) {
							resolve({});
						} else {
							reject(new Error(event.state.current));
						}
						browser.downloads.onChanged.removeListener(onChanged);
					}
				}
			}
		});
	}

	function saveToClipboard(pageData) {
		const command = "copy";
		document.addEventListener(command, listener);
		document.execCommand(command);
		document.removeEventListener(command, listener);

		function listener(event) {
			event.clipboardData.setData(MIMETYPE_HTML, pageData.content);
			event.clipboardData.setData("text/plain", pageData.content);
			event.preventDefault();
		}
	}

})();
