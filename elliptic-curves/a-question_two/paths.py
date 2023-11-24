from sage.all import *


def neighbours(j):
    F = GF(2).algebraic_closure()
    R.<x> = PolynomialRing(F, 'x')
    f = j ^ 3 + x ^ 3 - j ^ 2 * x ^ 2 + 1488 * (x ^ 2 * j + j ^ 2 * x) - 162000 * (
                x ^ 2 + j ^ 2) + 40773375 * x * j + 8748000000 * (x + j) - 157464000000000
    roots = [r for (r,m) in f.roots()]
    return f.roots()

def nb_path(j1, j2, n):
    j = [j1, j2]
    if n>= 3:
        for k in range(2, n-1):
            neigh = neighbours(j[k-1])
            if neigh[0] == j[k-2]:
                j.append(neigh[1])
            else:
                j.append(neigh[0])
    return j