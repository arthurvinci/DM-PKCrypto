from sage.all import *


def neighbours(j, field, verbose=False):
    R = PolynomialRing(field, 'x')
    x = R.gen()
    f = j ** 3 + x ** 3 - j ** 2 * x ** 2 + 1488 * (x ** 2 * j + j ** 2 * x) - 162000 * (
            x ** 2 + j ** 2) + 40773375 * x * j + 8748000000 * (x + j) - 157464000000000
    roots = [r for (r, m) in f.roots()]
    if verbose:
        print("Phi2 = {} has roots {}".format(f, roots))
    return roots


def nb_path(j1, j2, n, field, verbose=False):
    j = [j1, j2]
    if n >= 3:
        for k in range(2, n - 1):
            neigh = neighbours(j[k - 1], field, verbose)
            if neigh[0] == j[k - 2]:
                j.append(neigh[1])
            else:
                j.append(neigh[0])
    return j
