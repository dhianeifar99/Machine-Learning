import numpy as np

from WarmUp.WarmUpAssignment import warmup
from PlotData.plotdata import plot_data
from ComputeCost.computeCost import compute_Cost


def ex1():

    """
        Machine Learning Online Class - Exercise 1: Linear Regression
    """

    # ==================== Part 1: Basic Function ====================

    print('Running warmUp exercise ... ')
    print('5x5 Identity Matrix:')
    print(warmup(4))
    print('Program paused. Press enter to continue.')
    input()

    # ======================= Part 2: Plotting =======================

    print('Plotting Data ...')
    data = np.loadtxt('ex1data1.txt', delimiter=',')

    X = np.array([data[:, 0]], dtype=float).T    # X: population of a city
    y = np.array([data[:, 1]], dtype=float).T    # y: profit of a food truck in that city
    m = X.shape[0]  # m is the number of training examples

    plot_data(X, y)
    print('Program paused. Press enter to continue.')
    input()

    # =================== Part 3: Cost and Gradient descent ===================

    X = np.concatenate((np.ones((m, 1)), X), axis=1, dtype=float)

    theta = np.zeros((2, 1), dtype=float)

    iterations = 1500
    alpha = 0.01

    print('Testing the cost function ...')

    J = compute_Cost(X, y, theta)
    print('With theta = \n[0, 0]\nCost computed = {:.2f}'.format(J))
    print('Expected cost value (approx) 32.07')



if __name__ == '__main__':
    ex1()
