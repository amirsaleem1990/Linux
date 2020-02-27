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

/* global browser, document, prompt, getComputedStyle, addEventListener, removeEventListener, requestAnimationFrame, setTimeout, getSelection, Node */

this.singlefile.extension.ui.content.main = this.singlefile.extension.ui.content.main || (() => {

	const SELECTED_CONTENT_ATTRIBUTE_NAME = this.singlefile.lib.helper.SELECTED_CONTENT_ATTRIBUTE_NAME;

	const MASK_TAGNAME = "singlefile-mask";
	const PROGRESS_BAR_TAGNAME = "singlefile-progress-bar";
	const PROGRESS_CURSOR_TAGNAME = "singlefile-progress-cursor";
	const SELECTION_ZONE_TAGNAME = "single-file-selection-zone";
	const LOGS_WINDOW_TAGNAME = "singlefile-logs-window";
	const LOGS_LINE_TAGNAME = "singlefile-logs-line";
	const LOGS_LINE_ELEMENT_TAGNAME = "singlefile-logs-element";
	const SINGLE_FILE_UI_ELEMENT_CLASS = "single-file-ui-element";
	const SELECT_PX_THRESHOLD = 8;
	const LOG_PANEL_DEFERRED_IMAGES_MESSAGE = browser.i18n.getMessage("logPanelDeferredImages");
	const LOG_PANEL_FRAME_CONTENTS_MESSAGE = browser.i18n.getMessage("logPanelFrameContents");
	const LOG_PANEL_STEP_MESSAGE = browser.i18n.getMessage("logPanelStep");
	const LOG_PANEL_WIDTH = browser.i18n.getMessage("logPanelWidth");

	let selectedAreaElement;

	let logsWindowElement = createLogsWindowElement();
	const allProperties = new Set();
	Array.from(getComputedStyle(document.body)).forEach(property => allProperties.add(property));

	return {
		getSelectedLinks,
		markSelection,
		unmarkSelection,
		prompt(message, defaultValue) {
			return prompt(message, defaultValue);
		},
		onStartPage(options) {
			let maskElement = document.querySelector(MASK_TAGNAME);
			if (!maskElement) {
				if (options.logsEnabled) {
					document.body.appendChild(logsWindowElement);
					setLogsWindowStyle();
				}
				if (options.shadowEnabled) {
					const maskElement = createMaskElement();
					if (options.progressBarEnabled) {
						createProgressBarElement(maskElement);
					}
					maskElement.offsetWidth;
					maskElement.style.setProperty("background-color", "black", "important");
					maskElement.style.setProperty("opacity", .3, "important");
					document.body.offsetWidth;
				}
			}
		},
		onEndPage() {
			const maskElement = document.querySelector(MASK_TAGNAME);
			if (maskElement) {
				maskElement.remove();
			}

			logsWindowElement.remove();
			clearLogs();
		},
		onLoadResource(index, maxIndex, options) {
			if (options.shadowEnabled && options.progressBarEnabled) {
				const progressBarElement = document.querySelector(PROGRESS_BAR_TAGNAME);
				if (progressBarElement && maxIndex) {
					const width = Math.floor((index / maxIndex) * 100) + "%";
					if (progressBarElement.style.getPropertyValue("width") != width) {
						requestAnimationFrame(() => progressBarElement.style.setProperty("width", Math.floor((index / maxIndex) * 100) + "%", "important"));
					}
				}
			}
		},
		onLoadingDeferResources(options) {
			updateLog("load-deferred-images", LOG_PANEL_DEFERRED_IMAGES_MESSAGE, "…", options);
		},
		onLoadDeferResources(options) {
			updateLog("load-deferred-images", LOG_PANEL_DEFERRED_IMAGES_MESSAGE, "✓", options);
		},
		onLoadingFrames(options) {
			updateLog("load-frames", LOG_PANEL_FRAME_CONTENTS_MESSAGE, "…", options);
		},
		onLoadFrames(options) {
			updateLog("load-frames", LOG_PANEL_FRAME_CONTENTS_MESSAGE, "✓", options);
		},
		onStartStage(step, options) {
			updateLog("step-" + step, `${LOG_PANEL_STEP_MESSAGE} ${step + 1} / 3`, "…", options);
		},
		onEndStage(step, options) {
			updateLog("step-" + step, `${LOG_PANEL_STEP_MESSAGE} ${step + 1} / 3`, "✓", options);
		},
		onPageLoading() { },
		onLoadPage() { },
		onStartStageTask() { },
		onEndStageTask() { }
	};

	function getSelectedLinks() {
		let selectionFound;
		const links = [];
		const selection = getSelection();
		for (let indexRange = 0; indexRange < selection.rangeCount; indexRange++) {
			let range = selection.getRangeAt(indexRange);
			if (range && range.commonAncestorContainer) {
				const treeWalker = document.createTreeWalker(range.commonAncestorContainer);
				let rangeSelectionFound = false;
				let finished = false;
				while (!finished) {
					if (rangeSelectionFound || treeWalker.currentNode == range.startContainer || treeWalker.currentNode == range.endContainer) {
						rangeSelectionFound = true;
						if (range.startContainer != range.endContainer || range.startOffset != range.endOffset) {
							selectionFound = true;
							if (treeWalker.currentNode.tagName == "A" && treeWalker.currentNode.href) {
								links.push(treeWalker.currentNode.href);
							}
						}
					}
					if (treeWalker.currentNode == range.endContainer) {
						finished = true;
					} else {
						treeWalker.nextNode();
					}
				}
				if (selectionFound && treeWalker.currentNode == range.endContainer && treeWalker.currentNode.querySelectorAll) {
					treeWalker.currentNode.querySelectorAll("*").forEach(descendantElement => {
						if (descendantElement.tagName == "A" && descendantElement.href) {
							links.push(treeWalker.currentNode.href);
						}
					});
				}
			}
		}
		return Array.from(new Set(links));
	}

	async function markSelection(optionallySelected) {
		let selectionFound = markSelectedContent();
		if (selectionFound || optionallySelected) {
			return selectionFound;
		} else {
			selectionFound = await selectArea();
			if (selectionFound) {
				return markSelectedContent();
			}
		}
	}

	function markSelectedContent() {
		const selection = getSelection();
		let selectionFound;
		for (let indexRange = 0; indexRange < selection.rangeCount; indexRange++) {
			let range = selection.getRangeAt(indexRange);
			if (range && range.commonAncestorContainer) {
				const treeWalker = document.createTreeWalker(range.commonAncestorContainer);
				let rangeSelectionFound = false;
				let finished = false;
				while (!finished) {
					if (rangeSelectionFound || treeWalker.currentNode == range.startContainer || treeWalker.currentNode == range.endContainer) {
						rangeSelectionFound = true;
						if (range.startContainer != range.endContainer || range.startOffset != range.endOffset) {
							selectionFound = true;
							markSelectedNode(treeWalker.currentNode);
						}
					}
					if (selectionFound && treeWalker.currentNode == range.startContainer) {
						markSelectedParents(treeWalker.currentNode);
					}
					if (treeWalker.currentNode == range.endContainer) {
						finished = true;
					} else {
						treeWalker.nextNode();
					}
				}
				if (selectionFound && treeWalker.currentNode == range.endContainer && treeWalker.currentNode.querySelectorAll) {
					treeWalker.currentNode.querySelectorAll("*").forEach(descendantElement => markSelectedNode(descendantElement));
				}
			}
		}
		return selectionFound;
	}

	function markSelectedNode(node) {
		const element = node.nodeType == Node.ELEMENT_NODE ? node : node.parentElement;
		element.setAttribute(SELECTED_CONTENT_ATTRIBUTE_NAME, "");
	}

	function markSelectedParents(node) {
		if (node.parentElement) {
			markSelectedNode(node);
			markSelectedParents(node.parentElement);
		}
	}

	function unmarkSelection() {
		document.querySelectorAll("[" + SELECTED_CONTENT_ATTRIBUTE_NAME + "]").forEach(selectedContent => selectedContent.removeAttribute(SELECTED_CONTENT_ATTRIBUTE_NAME));
	}

	function selectArea() {
		return new Promise(resolve => {
			let selectedRanges = [];
			addEventListener("mousemove", mousemoveListener, true);
			addEventListener("click", clickListener, true);
			addEventListener("keyup", keypressListener, true);
			document.addEventListener("contextmenu", contextmenuListener, true);
			getSelection().removeAllRanges();

			function contextmenuListener(event) {
				selectedRanges = [];
				select();
				event.preventDefault();
			}

			function mousemoveListener(event) {
				const targetElement = getTarget(event);
				if (targetElement) {
					selectedAreaElement = targetElement;
					moveAreaSelector(targetElement);
				}
			}

			function clickListener(event) {
				event.preventDefault();
				event.stopPropagation();
				if (event.button == 0) {
					select(selectedAreaElement, event.ctrlKey);
				} else {
					cancel();
				}
			}

			function keypressListener(event) {
				if (event.key == "Escape") {
					cancel();
				}
			}

			function cancel() {
				if (selectedRanges.length) {
					getSelection().removeAllRanges();
				}
				selectedRanges = [];
				cleanupAndResolve();
			}

			function select(selectedElement, multiSelect) {
				if (selectedElement) {
					if (!multiSelect) {
						restoreSelectedRanges();
					}
					const range = document.createRange();
					range.selectNodeContents(selectedElement);
					cleanupSelectionRanges();
					getSelection().addRange(range);
					saveSelectedRanges();
					if (!multiSelect) {
						cleanupAndResolve();
					}
				} else {
					cleanupAndResolve();
				}
			}

			function cleanupSelectionRanges() {
				const selection = getSelection();
				for (let indexRange = selection.rangeCount - 1; indexRange >= 0; indexRange--) {
					const range = selection.getRangeAt(indexRange);
					if (range.startOffset == range.endOffset) {
						selection.removeRange(range);
						indexRange--;
					}
				}
			}

			function cleanupAndResolve() {
				getAreaSelector().remove();
				removeEventListener("mousemove", mousemoveListener, true);
				removeEventListener("click", clickListener, true);
				removeEventListener("keyup", keypressListener, true);
				selectedAreaElement = null;
				resolve(Boolean(selectedRanges.length));
				setTimeout(() => document.removeEventListener("contextmenu", contextmenuListener, true), 0);
			}

			function restoreSelectedRanges() {
				getSelection().removeAllRanges();
				selectedRanges.forEach(range => getSelection().addRange(range));
			}

			function saveSelectedRanges() {
				selectedRanges = [];
				for (let indexRange = 0; indexRange < getSelection().rangeCount; indexRange++) {
					const range = getSelection().getRangeAt(indexRange);
					selectedRanges.push(range);
				}
			}
		});
	}

	function getTarget(event) {
		let newTarget, target = event.target, boundingRect = target.getBoundingClientRect();
		newTarget = determineTargetElement("floor", target, event.clientX - boundingRect.left, getMatchedParents(target, "left"));
		if (newTarget == target) {
			newTarget = determineTargetElement("ceil", target, boundingRect.left + boundingRect.width - event.clientX, getMatchedParents(target, "right"));
		}
		if (newTarget == target) {
			newTarget = determineTargetElement("floor", target, event.clientY - boundingRect.top, getMatchedParents(target, "top"));
		}
		if (newTarget == target) {
			newTarget = determineTargetElement("ceil", target, boundingRect.top + boundingRect.height - event.clientY, getMatchedParents(target, "bottom"));
		}
		target = newTarget;
		while (target && target.clientWidth <= SELECT_PX_THRESHOLD && target.clientHeight <= SELECT_PX_THRESHOLD) {
			target = target.parentElement;
		}
		return target;
	}

	function moveAreaSelector(target) {
		requestAnimationFrame(() => {
			const selectorElement = getAreaSelector();
			const boundingRect = target.getBoundingClientRect();
			const scrollingElement = document.scrollingElement || document.documentElement;
			selectorElement.style.setProperty("top", (scrollingElement.scrollTop + boundingRect.top - 10) + "px");
			selectorElement.style.setProperty("left", (scrollingElement.scrollLeft + boundingRect.left - 10) + "px");
			selectorElement.style.setProperty("width", (boundingRect.width + 20) + "px");
			selectorElement.style.setProperty("height", (boundingRect.height + 20) + "px");
		});
	}

	function getAreaSelector() {
		let selectorElement = document.querySelector(SELECTION_ZONE_TAGNAME);
		if (!selectorElement) {
			selectorElement = createElement(SELECTION_ZONE_TAGNAME, document.body);
			selectorElement.style.setProperty("box-sizing", "border-box", "important");
			selectorElement.style.setProperty("background-color", "#3ea9d7", "important");
			selectorElement.style.setProperty("border", "10px solid #0b4892", "important");
			selectorElement.style.setProperty("border-radius", "2px", "important");
			selectorElement.style.setProperty("opacity", ".25", "important");
			selectorElement.style.setProperty("pointer-events", "none", "important");
			selectorElement.style.setProperty("position", "absolute", "important");
			selectorElement.style.setProperty("transition", "all 100ms", "important");
			selectorElement.style.setProperty("cursor", "pointer", "important");
			selectorElement.style.setProperty("z-index", "2147483647", "important");
			selectorElement.style.removeProperty("border-inline-end");
			selectorElement.style.removeProperty("border-inline-start");
			selectorElement.style.removeProperty("inline-size");
			selectorElement.style.removeProperty("block-size");
			selectorElement.style.removeProperty("inset-block-start");
			selectorElement.style.removeProperty("inset-inline-end");
			selectorElement.style.removeProperty("inset-block-end");
			selectorElement.style.removeProperty("inset-inline-start");
		}
		return selectorElement;
	}

	function createMaskElement() {
		let maskElement = document.querySelector(MASK_TAGNAME);
		if (!maskElement) {
			maskElement = createElement(MASK_TAGNAME, document.body);
			maskElement.style.setProperty("opacity", 0, "important");
			maskElement.style.setProperty("background-color", "transparent", "important");
			maskElement.offsetWidth;
			maskElement.style.setProperty("position", "fixed", "important");
			maskElement.style.setProperty("top", "0", "important");
			maskElement.style.setProperty("left", "0", "important");
			maskElement.style.setProperty("width", "100%", "important");
			maskElement.style.setProperty("height", "100%", "important");
			maskElement.style.setProperty("z-index", 2147483646, "important");
			maskElement.style.setProperty("transition", "opacity 250ms", "important");
		}
		return maskElement;
	}

	function createProgressBarElement(maskElement) {
		let progressBarElementContainer = document.querySelector(PROGRESS_BAR_TAGNAME);
		if (!progressBarElementContainer) {
			progressBarElementContainer = createElement(PROGRESS_BAR_TAGNAME, maskElement);
			const styleElement = document.createElement("style");
			styleElement.textContent = "@keyframes single-file-progress { 0% { left: -50px } 100% { left: 0 }";
			maskElement.appendChild(styleElement);
			progressBarElementContainer.style.setProperty("position", "fixed", "important");
			progressBarElementContainer.style.setProperty("top", "0", "important");
			progressBarElementContainer.style.setProperty("left", "0", "important");
			progressBarElementContainer.style.setProperty("width", "0", "important");
			progressBarElementContainer.style.setProperty("height", "8px", "important");
			progressBarElementContainer.style.setProperty("overflow", "hidden", "important");
			progressBarElementContainer.style.setProperty("transition", "width 200ms", "important");
			progressBarElementContainer.style.setProperty("will-change", "width", "important");
			const progressBarElement = createElement(PROGRESS_CURSOR_TAGNAME, progressBarElementContainer);
			progressBarElement.style.setProperty("position", "absolute", "important");
			progressBarElement.style.setProperty("left", "0");
			progressBarElement.style.setProperty("animation", "single-file-progress 5s linear infinite reverse", "important");
			progressBarElement.style.setProperty("background", "white linear-gradient(-45deg, rgba(0, 0, 0, 0.1) 25%, transparent 25%, transparent 50%, rgba(0, 0, 0, 0.1) 50%, rgba(0, 0, 0, 0.1) 75%, transparent 75%, transparent) repeat scroll 0% 0% / 50px 50px padding-box border-box", "important");
			progressBarElement.style.setProperty("width", "calc(100% + 50px)", "important");
			progressBarElement.style.setProperty("height", "100%", "important");
			progressBarElement.style.setProperty("inset-inline-start", "auto");
		}
		return progressBarElementContainer;
	}

	function createLogsWindowElement() {
		let logsWindowElement = document.querySelector(LOGS_WINDOW_TAGNAME);
		if (!logsWindowElement) {
			logsWindowElement = document.createElement(LOGS_WINDOW_TAGNAME);
			logsWindowElement.className = SINGLE_FILE_UI_ELEMENT_CLASS;
		}
		const styleElement = document.createElement("style");
		logsWindowElement.appendChild(styleElement);
		styleElement.textContent = "@keyframes single-file-pulse { 0% { opacity: .5 } 100% { opacity: 1 }";
		return logsWindowElement;
	}

	function setLogsWindowStyle() {
		initStyle(logsWindowElement);
		logsWindowElement.style.setProperty("opacity", "0.9", "important");
		logsWindowElement.style.setProperty("padding", "4px", "important");
		logsWindowElement.style.setProperty("position", "fixed", "important");
		logsWindowElement.style.setProperty("bottom", "24px", "important");
		logsWindowElement.style.setProperty("left", "8px", "important");
		logsWindowElement.style.setProperty("z-index", 2147483647, "important");
		logsWindowElement.style.setProperty("background-color", "white", "important");
		logsWindowElement.style.setProperty("min-width", LOG_PANEL_WIDTH + "px", "important");
		logsWindowElement.style.setProperty("min-height", "16px", "important");
		logsWindowElement.style.setProperty("transition", "height 100ms", "important");
		logsWindowElement.style.setProperty("will-change", "height", "important");
	}

	function updateLog(id, textContent, textStatus, options) {
		if (options.logsEnabled) {
			let lineElement = logsWindowElement.querySelector("[data-id='" + id + "']");
			if (!lineElement) {
				lineElement = createElement(LOGS_LINE_TAGNAME, logsWindowElement);
				lineElement.setAttribute("data-id", id);
				lineElement.style.setProperty("display", "flex", "important");
				lineElement.style.setProperty("justify-content", "space-between", "important");
				lineElement.style.setProperty("padding", "2px", "important");
				const textElement = createElement(LOGS_LINE_ELEMENT_TAGNAME, lineElement);
				textElement.style.setProperty("font-size", "13px", "important");
				textElement.style.setProperty("font-family", "arial, sans-serif", "important");
				textElement.style.setProperty("color", "black", "important");
				textElement.style.setProperty("background-color", "white", "important");
				textElement.style.setProperty("opacity", "1", "important");
				textElement.style.setProperty("transition", "opacity 200ms", "important");
				textElement.textContent = textContent;
				const statusElement = createElement(LOGS_LINE_ELEMENT_TAGNAME, lineElement);
				statusElement.style.setProperty("font-size", "11px", "important");
				statusElement.style.setProperty("font-family", "arial, sans-serif", "important");
				statusElement.style.setProperty("color", "black", "important");
				statusElement.style.setProperty("background-color", "white", "important");
				statusElement.style.setProperty("min-width", "15px", "important");
				statusElement.style.setProperty("text-align", "center", "important");
				statusElement.style.setProperty("position", "relative", "important");
				statusElement.style.setProperty("top", "1px", "important");
				statusElement.style.setProperty("will-change", "opacity", "important");
			}
			updateLogLine(lineElement, textContent, textStatus);
		}
	}

	function updateLogLine(lineElement, textContent, textStatus) {
		const textElement = lineElement.childNodes[0];
		const statusElement = lineElement.childNodes[1];
		textElement.textContent = textContent;
		statusElement.style.setProperty("color", textStatus == "✓" ? "#055000" : "black", "important");
		if (textStatus == "✓") {
			textElement.style.setProperty("opacity", ".5", "important");
			statusElement.style.setProperty("animation", "none", "important");
		} else {
			statusElement.style.setProperty("opacity", ".5", "important");
			statusElement.style.setProperty("animation", "single-file-pulse 1s linear infinite alternate", "important");
		}
		statusElement.textContent = textStatus;
	}

	function clearLogs() {
		logsWindowElement = createLogsWindowElement();
	}

	function getMatchedParents(target, property) {
		let element = target, matchedParent, parents = [];
		do {
			const boundingRect = element.getBoundingClientRect();
			if (element.parentElement) {
				const parentBoundingRect = element.parentElement.getBoundingClientRect();
				matchedParent = Math.abs(parentBoundingRect[property] - boundingRect[property]) <= SELECT_PX_THRESHOLD;
				if (matchedParent) {
					if (element.parentElement.clientWidth > SELECT_PX_THRESHOLD && element.parentElement.clientHeight > SELECT_PX_THRESHOLD &&
						((element.parentElement.clientWidth - element.clientWidth > SELECT_PX_THRESHOLD) || (element.parentElement.clientHeight - element.clientHeight > SELECT_PX_THRESHOLD))) {
						parents.push(element.parentElement);
					}
					element = element.parentElement;
				}
			} else {
				matchedParent = false;
			}
		} while (matchedParent && element);
		return parents;
	}

	function determineTargetElement(roundingMethod, target, widthDistance, parents) {
		if (Math[roundingMethod](widthDistance / SELECT_PX_THRESHOLD) <= parents.length) {
			target = parents[parents.length - Math[roundingMethod](widthDistance / SELECT_PX_THRESHOLD) - 1];
		}
		return target;
	}

	function createElement(tagName, parentElement) {
		const element = document.createElement(tagName);
		element.className = SINGLE_FILE_UI_ELEMENT_CLASS;
		parentElement.appendChild(element);
		initStyle(element);
		return element;
	}

	function initStyle(element) {
		allProperties.forEach(property => element.style.setProperty(property, "initial", "important"));
	}

})();
