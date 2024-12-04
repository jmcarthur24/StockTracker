function renderChart(labels, data) {
  const ctx = document.getElementById("stockChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Closing Price",
          data: data,
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 2,
          tension: 0.4,
          fill: false,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true },
      },
      scales: {
        x: { title: { display: true, text: "Date" } },
        y: { title: { display: true, text: "Price" } },
      },
    },
  });
}
