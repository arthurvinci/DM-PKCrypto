from sage.all import *

from dlog_questions.a_one.exponentiation import exp, exp_mod
from dlog_questions.d_four.baby_step_giant_step import baby_step_giant_step


def pohlig_hellman(p: int, g: int, h: int, verbose=False) -> int:
    N = p - 1
    factors = list(ZZ(N).factor())
    if verbose:
        print("N = {} has factors: {}".format(N, factors))
    residus = []
    facteurs = []
    for factor in factors:
        p_i, e_i = factor
        if verbose:
            print("Computing for factor {}^{}".format(p_i, e_i))
        fact = exp(p_i, e_i)
        N_i = N // fact
        g_i = exp_mod(g, N_i, p, verbose)
        h_i = exp_mod(h, N_i, p, verbose)
        x_i = baby_step_giant_step(g_i, h_i, p, verbose) % fact
        residus.append(x_i)
        facteurs.append(fact)

    if verbose:
        print("Residus: {}, facteurs: {}".format(residus, facteurs))

    sol = crt(residus, facteurs)
    if verbose:
        print("Solution: ", sol)
    return sol