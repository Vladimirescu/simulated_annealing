from scipy.optimize import dual_annealing
from time import time
from simulated_annealing import ackley, himmelblau, styblinski_tang, rastrigin
import numpy as np
import matplotlib.pyplot as plt
import cProfile


if __name__ == "__main__":

    bounds = np.array([[-5, 5], [-5, 5]])
    maxiter = 4600
    x_optim = np.array([0, 0])

    dt = []
    dist = []

    for _ in range(50):
        t0 = time()
        result = dual_annealing(ackley, bounds, maxiter=maxiter)
        t1 = time()

        print("Total time: ", t1 - t0, "seconds")

        dt.append(t1 - t0)
        dst = np.sqrt(np.sum((result.x - x_optim) ** 2))
        print(result.x)
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
