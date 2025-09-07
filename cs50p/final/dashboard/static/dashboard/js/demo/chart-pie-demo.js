// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

document.addEventListener("DOMContentLoaded", function () {
  const currentURL = window.location.pathname;
  if (currentURL.includes("/login") || currentURL.includes("/register")) {
    return;
  }

  // Make an AJAX request to the Django API
  fetch('/charts/transactions/')
      .then(response => response.json())
      .then(data => {
          // Extract income and expense data
          const totalIncome = data.pie_chart.total_income;
          const totalExpense = data.pie_chart.total_expense;

          // Initialize Chart.js
          const ctx = document.getElementById('myPieChart').getContext('2d');
          const budgetPieChart = new Chart(ctx, {
              type: 'doughnut', 
              data: {
                  labels: ['Income', 'Expenses'],
                  datasets: [
                      {
                          label: ['Income', 'Expences'],
                          data: [totalIncome, totalExpense],
                          backgroundColor: ['#4e73df', '#1cc88a'],
                          fill: false,
                      }
                  ]
              },
              options: {
                maintainAspectRatio: false,
              },
          });
      })
      .catch(error => console.error('Error fetching data:', error));
});

