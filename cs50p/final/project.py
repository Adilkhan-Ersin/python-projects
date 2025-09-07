"""
Graphing calculator
Name: Ersin Adilkhan
Almaty, Kazakhstan
16/07/2024
"""

from remote_plot import plt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.style.use('_mpl-gallery')
def main():
    choice = input("Do you want to enter a simple formula or quadratic equation? (enter 'f' or 'q'): ").strip().lower()
    if choice == 'f':
        formula = input("Enter a formula (# '4 * np.sin(2 * x)', 'x**2', etc.): ")
        plot_formula(formula)
    elif choice == 'q':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        root1, root2 = solve_quadratic(a, b, c)
        if root1 is not None and root2 is not None:
            print(f"The roots of the quadratic equation are: {root1} and {root2}")
        else:
            print("The quadratic equation has no real roots.")
        plot_quadratic(a, b, c)
# simple
def evaluate_formula(formula, x):
    return eval(formula)
# quadric
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    if D >= 0:
        root1 = (-b + np.sqrt(D)) / (2*a)
        root2 = (-b - np.sqrt(D)) / (2*a)
        return root1, root2
    else:
        return None, None
# simple showcase graph matplotlib
def plot_formula(formula, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    try:
        y = evaluate_formula(formula, x)
        fig, ax = plt.subplots(figsize=(5,3), layout='constrained')
        ax.plot(x, y, linewidth=2.0)
        ax.tick_params(color='red', labelcolor='green')
        ax.set_xlim(x.min(), 10)
        ax.set_ylim(y.min(), 20)
        ax.set_xticks(np.linspace(x.min(), 10, 10))
        ax.set_yticks(np.linspace(y.min(), 20, 10))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
        plt.savefig("graph.jpg")
    except Exception as e:
        print(f"Error evaluating formula: {e}")
# quadratic showcase graph matplotlib
def plot_quadratic(a, b, c, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = a * x**2 + b * x + c
    fig, ax = plt.subplots(figsize=(5,3), layout='constrained')
    ax.plot(x, y, linewidth=2.0)
    ax.tick_params(color='red', labelcolor='green')
    ax.set_xlim(x.min(), 10)
    ax.set_ylim(y.min(), 20)
    ax.set_xticks(np.linspace(x.min(), 10, 10))
    ax.set_yticks(np.linspace(y.min(), 20, 10))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
    plt.savefig("graph.jpg")

if __name__ == "__main__":
    main()
