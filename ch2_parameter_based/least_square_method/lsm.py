# -*- coding: utf-8 -*-

import fileinput

import matplotlib.pyplot as plt
import numpy as np


# Calculate linear regression based on least square method
class LSM:

    sxi = 0
    syi = 0
    sxiyi = 0
    sxi2 = 0
    n = 0

    list_xi = []
    list_yi = []

    def __init__(self):
        pass

    # Read data points
    def read(self, xi, yi):
        xi = float(xi)
        yi = float(yi)
        self.sxi += xi
        self.syi += yi
        self.sxiyi += xi * yi
        self.sxi2 += xi * xi
        self.n += 1
        self.list_xi.append(xi)
        self.list_yi.append(yi)
        pass

    # Calculate coefficient
    def calc_coefficient(self):
        if self.n > 1:
            a0 = (self.sxi2 * self.syi - self.sxiyi * self.sxi) / (self.n * self.sxi2 - self.sxi * self.sxi)
            a1 = (self.n * self.sxiyi - self.sxi * self.syi) / (self.n * self.sxi2 - self.sxi * self.sxi)
            return a0, a1
        else:
            raise RuntimeError('At least two input required')

    # Plot data points and graph
    def plot(self):
        cf = self.calc_coefficient()
        x = np.linspace(0, max(self.list_xi) + 1, 1000)
        plt.text(2, 3, 'y = %s + %s * x' % cf)
        plt.plot(self.list_xi, self.list_yi, 'ro', x, cf[0] + cf[1] * x)
        plt.show()


# Main starts here #####
lsm = LSM()

for line in fileinput.input():
    row = line.split()
    if len(row) != 2:
        raise RuntimeError('row must be pair of x and y')
    else:
        lsm.read(row[0], row[1])

print lsm.calc_coefficient()
print lsm.plot()
