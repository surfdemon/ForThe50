// hide link https://translate.yandex.com/
document.addEventListener("DOMContentLoaded", function () {
  const observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      const yandexLink = document.querySelector('a[href="https://translate.yandex.com/"]');
      if (yandexLink) {
        yandexLink.style.display = "none";
        observer.disconnect(); 
      }
    });
  });

  observer.observe(document.body, { childList: true, subtree: true });
});