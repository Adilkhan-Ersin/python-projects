# Financial Tracker Project
## Video Demo: [YouTube](https://youtu.be/dKk-h_CoFq8)
## Overview
This project is a comprehensive financial tracker that allows users to monitor their income and expenses through dynamic charts and tables. It also includes a goals feature that helps users set financial goals and track their progress toward achieving them. The application provides an intuitive interface for users to view detailed transaction histories, set financial targets, and visualize data through interactive charts.

## Distinctiveness and Complexity
This project stands out due to its integration of multiple features to manage personal finances. It not only tracks income and expenses but also allows users to visualize their financial data using both pie and line charts. The inclusion of goal-setting functionality adds an additional layer of complexity, allowing users to set, edit, and delete financial goals while tracking their progress through dynamically updated progress bars. Each goal is uniquely styled with randomly assigned colors for better visualization.

Additionally, the project involves complex backend logic for calculating percentages, managing transactions, and updating goals. This level of integration, along with the use of JavaScript for dynamic chart generation and goal management, ensures that the project satisfies the requirements of both distinctiveness and complexity.

## Project Structure
Here’s a breakdown of the main files and directories in the project:

- **Static Files**: Contains all JavaScript necessary for chart generation (pie and line charts) and the edit/delete functionality for goals. It also includes assets like CSS files, which utilize Bootstrap for styling.

- **Models**:
  - `User`: Manages user authentication and information.
  - `Post`: Represents goals that users can set.
  - `Transaction`: Handles income and expense data, used for generating charts and tables.

- **Views**: Includes functions for adding transactions, retrieving income/expense data, calculating percentages, assigning random colors to goals, and more.

- **Templates**:
  - Authentication-related templates: `login.html`, `register.html`, `forgot.html`
  - Main templates: `layout.html`, `index.html`
  - Error pages: `404.html`, `403.html`
  - Data display templates: `tables.html`, `charts.html`

## How to Run the Application
To run this application locally, follow these steps:

1. Clone the repository and navigate into the project directory.
2. In your terminal:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
Visit http://127.0.0.1:8000/ in your browser to use the application.
