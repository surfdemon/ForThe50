const currentYear = new Date().getFullYear();
document.getElementById("current-year").innerText = currentYear;

// Chatbot
document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("chatbot-toggle");
  const chatbotContainer = document.getElementById("chatbot-container");
  const chatbotMessages = document.getElementById("chatbot-messages");
  const chatbotInput = document.getElementById("chatbot-input");
  const chatbotSend = document.getElementById("chatbot-send");

  toggleButton.addEventListener("click", () => {
    chatbotContainer.style.display =
      chatbotContainer.style.display === "none" ? "block" : "none";
  });

  chatbotSend.addEventListener("click", async () => {
    const userMessage = chatbotInput.value.trim();
    if (userMessage) {
      const userMessageElement = document.createElement("div");
      userMessageElement.textContent = `You: ${userMessage}`;
      chatbotMessages.appendChild(userMessageElement);

      try {
        const response = await fetch("/chatbot/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body: JSON.stringify({ message: userMessage }),
        });
        const data = await response.json();
        const botMessageElement = document.createElement("div");
        botMessageElement.textContent = `Bot: ${data.response}`;
        chatbotMessages.appendChild(botMessageElement);
      } catch (error) {
        const errorMessage = document.createElement("div");
        errorMessage.textContent = "Bot: Sorry, something went wrong.";
        chatbotMessages.appendChild(errorMessage);
      }
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
      chatbotInput.value = "";
    }
  });

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
  }
});

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
