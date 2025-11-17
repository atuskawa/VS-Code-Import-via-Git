const quotes = [
  "Speed is everything, but accuracy matters more.",
  "You can’t improve what you don’t measure.",
  "Type fast, think faster.",
  "Perfection comes with practice."
];

const quoteDisplay = document.getElementById("quote");
const input = document.getElementById("input");
const timerDisplay = document.getElementById("timer");
const wpmDisplay = document.getElementById("wpm");
const accuracyDisplay = document.getElementById("accuracy");
const restartBtn = document.getElementById("restart");

let startTime, timer, currentQuote, mistakes = 0;

function newQuote() {
  currentQuote = quotes[Math.floor(Math.random() * quotes.length)];
  quoteDisplay.innerText = currentQuote;
  input.value = "";
  mistakes = 0;
  clearInterval(timer);
  timerDisplay.textContent = "0s";
  wpmDisplay.textContent = "0 WPM";
  accuracyDisplay.textContent = "100%";
}

input.addEventListener("input", () => {
  const text = input.value;
  if (!startTime) {
    startTime = new Date();
    timer = setInterval(updateTimer, 1000);
  }

  let correctChars = 0;
  for (let i = 0; i < text.length; i++) {
    if (text[i] === currentQuote[i]) correctChars++;
  }

  mistakes = text.length - correctChars;

  const accuracy = ((correctChars / text.length) * 100).toFixed(0) || 100;
  accuracyDisplay.textContent = accuracy + "%";

  if (text === currentQuote) {
    clearInterval(timer);
    calculateWPM();
  }
});

function updateTimer() {
  const seconds = Math.floor((new Date() - startTime) / 1000);
  timerDisplay.textContent = seconds + "s";
}

function calculateWPM() {
  const timeTaken = (new Date() - startTime) / 1000 / 60; // minutes
  const words = currentQuote.split(" ").length;
  const wpm = Math.round(words / timeTaken);
  wpmDisplay.textContent = wpm + " WPM";
}

restartBtn.addEventListener("click", () => {
  startTime = null;
  newQuote();
});

newQuote();
