chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "open-selected-links",
    title: "선택한 링크들 새 탭에서 열기",
    contexts: ["selection"]
  });
});

chrome.runtime.onStartup.addListener(() => {
  chrome.contextMenus.create({
    id: "open-selected-links",
    title: "선택한 링크들 새 탭에서 열기",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "open-selected-links") {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        const selection = window.getSelection();
        const container = document.createElement("div");
        for (let i = 0; i < selection.rangeCount; i++) {
          container.appendChild(selection.getRangeAt(i).cloneContents());
        }

        const links = container.querySelectorAll("a[href]");
        const urls = Array.from(links).map(a => a.href);
        urls.forEach(url => window.open(url, "_blank"));
      }
    });
  }
});
