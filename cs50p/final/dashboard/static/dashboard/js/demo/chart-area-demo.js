// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Montserrat', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#000000';

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
          const incomeData = data.line_chart.income_data;
          const expenseData = data.line_chart.expense_data;

          // Prepare labels and data for Chart.js
          const labels = incomeData.map(item => item[0]); 
          const incomeAmounts = incomeData.map(item => item[1]); 
          const expenseAmounts = expenseData.map(item => item[1]);

          // Initialize Chart.js
          const ctx = document.getElementById('myAreaChart').getContext('2d');
          const budgetChart = new Chart(ctx, {
              type: 'line', 
              data: {
                  labels: labels,
                  datasets: [
                      {
                          label: 'Income',
                          data: incomeAmounts,
                          borderColor: 'green',
                          fill: false,
                      },
                      {
                          label: 'Expenses',
                          data: expenseAmounts,
                          borderColor: 'red',
                          fill: false,
                      }
                  ]
              },
              options: {
                  maintainAspectRatio: false,
                  scales: {
                      x: {
                          type: 'time', 
                          time: {
                              unit: 'day'
                          }
                      },
                      y: {
                          beginAtZero: true
                      }
                  }
              }
          });
      })
      .catch(error => console.error('Error fetching data:', error));
});
