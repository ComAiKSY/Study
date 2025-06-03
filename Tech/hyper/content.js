// 다운로드 버튼 자동 클릭
window.addEventListener("load", () => {
  const tryClickDownload = () => {
    const downloadButton = document.querySelector("button.link-button");
    if (downloadButton) {
      console.log("[확장] DOWNLOAD 버튼 클릭 성공");
      downloadButton.click();
    } else {
      console.log("[확장] 버튼 못 찾음, 재시도...");
      setTimeout(tryClickDownload, 1000);
    }
  };

  tryClickDownload();
});
