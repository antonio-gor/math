import matplotlib.pyplot as plt
import numpy as np

from math import gcd

#### Utilities ####

def plot(fn, start, stop):
    range = fn(start, stop)
    domain = np.linspace(start, stop, len(range))

    plt.figure()
    plt.plot(domain, range, 'k.', markersize=2)
    plt.title(fn.__name__)
    plt.grid(True)
    plt.show()

#### Sequences ####

def fly_straight_dammit(start=0, stop=1000):
    """ http://oeis.org/A133058 """

    def calculate(n, range_n_minus_1):
        if gcd(n, range_n_minus_1) == 1:
            return range_n_minus_1 + n + 1
        else:
            return int(range_n_minus_1 / gcd(n, range_n_minus_1))
    
    range = np.array([1, 1])
    n = 2
    while n <= stop:
        a = calculate(n, range[n-1])
        range = np.append(range, a)
        n += 1
    return range
