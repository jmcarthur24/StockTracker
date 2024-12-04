document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("stockForm");
  const tickerInput = document.getElementById("ticker");

  form.addEventListener("submit", function (event) {
    if (!tickerInput.value.trim()) {
      event.preventDefault();
      alert("Please enter a valid stock ticker.");
    }
  });
});
