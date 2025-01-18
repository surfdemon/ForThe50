const currentYear = new Date().getFullYear();
document.getElementById("current-year").innerText = currentYear;

// Ireland and UK Buttons
document.addEventListener("DOMContentLoaded", () => {
  const irelandData = document.getElementById("irelandData");
  const ukData = document.getElementById("ukData");
  const irelandButton = document.getElementById("irelandButton");
  const ukButton = document.getElementById("ukButton");

  irelandButton.addEventListener("click", () => {
    irelandData.classList.remove("d-none");
    ukData.classList.add("d-none");
    irelandButton.classList.add("btn-primary");
    irelandButton.classList.remove("btn-secondary");
    ukButton.classList.add("btn-secondary");
    ukButton.classList.remove("btn-primary");
  });

  ukButton.addEventListener("click", () => {
    irelandData.classList.add("d-none");
    ukData.classList.remove("d-none");
    ukButton.classList.add("btn-primary");
    ukButton.classList.remove("btn-secondary");
    irelandButton.classList.add("btn-secondary");
    irelandButton.classList.remove("btn-primary");
  });
});
