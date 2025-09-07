# Graphing calculator
#### Video Demo: [YouTube](https://youtu.be/-OZEU41TUkM)
#### Description:
This Python project allows users to plot graphs of mathematical formulas, including quadratic equations, using Matplotlib. The project provides functionality to evaluate and plot user-defined formulas and quadratic equations with specified coefficients.

## Features
- Plot any mathematical formula involving `x` (e.g., `4 + 1 * np.sin(2 * x)`, `x**2`, etc.).
- Solve and plot quadratic equations given coefficients `a`, `b`, and `c`.
- Adjustable x-axis and y-axis limits for better visualization.

## Installation
To get started with this project, you need to have Python installed. You can install the required dependencies using pip:
```
pip install matplotlib numpy pytest
```
## Usage
You can run the project by executing the main script:
```
python project.py
```
### Example
1. Run the script:
```
python project.py
```
2. Choose the type of input:
   - Enter `f` to input a simple formula.
   - Enter `q` to input a quadratic equation.
3. Input your formula or coefficients when prompted.

### Functions
`evaluate_formula(formula, x)`
Evaluates a given formula for an array of `x` values.

- Parameters:
  - `formula` (str): The mathematical formula as a string.
  - `x` (numpy.ndarray): The array of `x` values.
- Returns:
  - The evaluated result as a numpy array.

`solve_quadratic(a, b, c)`
Solves a quadratic equation given coefficients `a`, `b`, and `c`.

- Parameters:
  - `a` (float): Coefficient of `x^2`.
  - `b` (float): Coefficient of `x`.
  - `c` (float): Constant term.

- Returns:
  - The two roots of the quadratic equation, or `None` if there are no real roots.

`plot_formula(formula, x_range=(-10, 10), num_points=1000)`
Plots the graph of a given formula within a specified range.

- Parameters:
  - `formula` (str): The mathematical formula as a string.
  - `x_range` (tuple): The range of `x` values (default is `(-10, 10)`).
  - `num_points` (int): Number of points to generate for plotting (default is `1000`).

`plot_quadratic(a, b, c, x_range=(-10, 10), num_points=1000)`
Plots the graph of a quadratic equation given coefficients `a`, `b`, and `c`.

- Parameters:
  - `a` (float): Coefficient of `x^2`.
  - `b` (float): Coefficient of `x`.
  - `c` (float): Constant term.
  - `x_range` (tuple): The range of `x` values (default is `(-10, 10)`).
  - `num_points` (int): Number of points to generate for plotting (default is `1000`).

## Acknowledgements
This project utilizes the following libraries:

- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
