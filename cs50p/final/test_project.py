import pytest
import numpy as np
from project import evaluate_formula, solve_quadratic, plot_formula, plot_quadratic

def main():
  test_simple_formula()
  test_quad_formula()
  test_plot_formula()
  test_plot_quadratic


def test_simple_formula():
  x = np.array([0, 1, 2, 3])
  assert np.allclose(evaluate_formula('x**2', x), np.array([0, 1, 4, 9]))
  assert np.allclose(evaluate_formula('4 + np.sin(2*x)', x), 4 + np.sin(2 * x))

def test_quad_formula():
  root1, root2 = solve_quadratic(1, -3, 2)
  assert np.allclose([root1, root2], [2, 1])

  root1, root2 = solve_quadratic(1, 0, -4)
  assert np.allclose([root1, root2], [2, -2])

  root1, root2 = solve_quadratic(1, 0, 4)
  assert root1 is None and root2 is None

def test_plot_formula():
  try:
      plot_formula('x**2')
  except Exception as e:
      pytest.fail(f"plot_formula raised an exception: {e}")


def test_plot_quadratic():
  try:
      plot_quadratic(1, -3, 2)
  except Exception as e:
      pytest.fail(f"plot_quadratic raised an exception: {e}")


if __name__ == "__main__":
  main()
