// Ireland and UK Buttons
document.addEventListener("DOMContentLoaded", () => {
  const irelandData = document.getElementById("irelandData");
  const ukData = document.getElementById("ukData");
  const irelandButton = document.getElementById("irelandButton");
  const ukButton = document.getElementById("ukButton");

  irelandButton.addEventListener("click", () => {
    irelandData.classList.remove("d-none");
    ukData.classList.add("d-none");
    irelandButton.classList.add("primary-btn");
    irelandButton.classList.remove("inactive-btn");
    ukButton.classList.add("inactive-btn");
    ukButton.classList.remove("primary-btn");
  });

  ukButton.addEventListener("click", () => {
    irelandData.classList.add("d-none");
    ukData.classList.remove("d-none");
    ukButton.classList.add("primary-btn");
    ukButton.classList.remove("inactive-btn");
    irelandButton.classList.add("inactive-btn");
    irelandButton.classList.remove("primary-btn");
  });
});

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