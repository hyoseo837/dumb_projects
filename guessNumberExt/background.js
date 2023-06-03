let kkk = 10;

chrome.runtime.onInstalled.addListener(() => {
    chrome.storage.sync.set({kkk});
    console.log(kkk);
})