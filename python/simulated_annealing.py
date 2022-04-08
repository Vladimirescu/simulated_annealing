import numpy as np
import matplotlib.pyplot as plt
from time import time
import cProfile
from tqdm import tqdm
import ctypes as ct
import seaborn as sns


mymodule = ct.CDLL("./ackley.dll")
himmelblau_c = ct.CDLL("./himmelblau.dll")
styblinski_c = ct.CDLL("./styblinski.dll")
rastrigini_c = ct.CDLL("./rastrigini.dll")


def call_ackley_C(arr_in):

    point = ct.POINTER(ct.c_float)
    x = np.array([0], np.single)
    pointr = arr_in.ctypes.data_as(point)

    mymodule.ackley(pointr, x.ctypes.data_as(point))

    return x[0]


def call_himmelblau_C(arr_in):
    point = ct.POINTER(ct.c_float)
    x = np.array([0], np.single)
    pointr = arr_in.ctypes.data_as(point)

    himmelblau_c.himmelblau(pointr, x.ctypes.data_as(point))

    return x[0]


def call_styblinski_C(arr_in):
    point = ct.POINTER(ct.c_float)
    x = np.array([0], np.single)
    pointr = arr_in.ctypes.data_as(point)

    styblinski_c.styblinski_tang(pointr, x.ctypes.data_as(point))

    return x[0]


def call_rastrigini_C(arr_in):
    point = ct.POINTER(ct.c_float)
    x = np.array([0], np.single)
    pointr = arr_in.ctypes.data_as(point)

    rastrigini_c.rastrigini(pointr, x.ctypes.data_as(point))

    return x[0]


def ackley(x):
    f1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * np.sum(x**2)))
    f2 = -np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])))
    return f1 + f2 + np.e + 20


def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2


def styblinski_tang(x):
    return (x[0]**4 - 16 * x[0]**2 + 5 * x[0]) / 2 + (x[1] ** 4 - 16 * x[1]**2 + 5 * x[1]) / 2


def rastrigin(x):
    return 20 + (x[0]**2 - 10 * np.cos(2 * np.pi * x[0])) + (x[1]**2 - 10 * np.cos(2 * np.pi * x[1]))


def booth(x):
    return (x[0] + 2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2


def quadratic(x):
    return np.sum(x**2)


def easy(x):
    return x**2


def get_neighbour(x, bounds):

    n = x + np.random.randn(len(x)).astype(np.single)
    if len(bounds.shape) == 1:
        n = np.clip(n, bounds[0], bounds[1])
    else:
        for i, b in enumerate(bounds):
            n[i] = np.clip(n[i], b[0], b[1])
    return n


def SA(bounds, x_optim, f, T0, iters_T=10):
    x = np.empty_like(x_optim)

    if len(bounds.shape) == 1:
        x = np.random.uniform(low=bounds[0], high=bounds[1])
    else:
        for i, b in enumerate(bounds):
            x[i] = np.random.uniform(low=b[0], high=b[1])

    T = T0
    x = x.astype(np.single)
    x_new = x
    while T > 1e-3:
        for _ in range(iters_T):
            yk = get_neighbour(x_new, bounds)
            r = np.random.uniform(low=0, high=1)

            if f(yk) > f(x_new):
                p = np.exp(-(f(yk) - f(x_new)) / T)
                if p > r:
                    x_new = yk

            if f(yk) < f(x_new):
                x_new = yk

        T = T * 0.997

    return x_new


if __name__ == "__main__":

    bounds = np.array([[-5, 5], [-5, 5]])
    x_optim = np.array([0, 0])
    T0 = 1000

    diffs = []
    n_eps = []
    sols = []
    best_solution = None
    diff_best = None

    dt = []
    dist = []

    print(styblinski_tang([-2.9, -2.9]))

    # print("Time analysis: ")
    # cProfile.run("SA(bounds, x_optim, himmelblau, T0)")

    # print("Time analysis Ctypes: ")
    # cProfile.run("SA(bounds, x_optim, call_ackley_C, T0)")

    for _ in range(100):
        t0 = time()
        x = SA(bounds, x_optim, call_himmelblau_C, T0)
        t1 = time()
        print("Total time: ", t1 - t0, "seconds")

        print(x)
        dt.append(t1 - t0)
        dst = np.sqrt(np.sum((x - x_optim)**2))
        dist.append(dst)

    print("Medie: ", np.mean(dt))
    print("Dispersie: ", np.std(dt))
    print("Distanța medie față de soluție: ", np.mean(dist))

    # plt.figure()
    # plt.hist(dt, color='green', rwidth=0.9)
    # plt.xlabel("Timp (s)")
    # plt.ylabel("Frecvență apariție")
    # plt.grid()
    # plt.show()

