from sage.all import *

from dlog.questions.one.exponentiation import exp, exp_mod


def floyd_step(a_n: int, b_n: int, x_n: int, g: int, h: int, p: int) -> (int, int, int):
    if h == 1:
        return (a_n + 1) % (p - 1), b_n, (x_n * g) % p
    match x_n % 3:
        case 0:
            return (a_n + 1) % (p - 1), b_n, (x_n * g) % p
        case 1:
            return (2 * a_n) % (p - 1), (2 * b_n) % (p - 1), (x_n ** 2) % p
        case 2:
            return a_n, (b_n + 1) % (p - 1), (x_n * h) % p


def rho_floyd(g: int, h: int, p: int) -> (int, int):
    x, alpha, beta = h, 0, 1
    y, gamma, delta = h, 0, 1
    while True:
        alpha, beta, x = floyd_step(alpha, beta, x, g, h, p)
        gamma, delta, y = floyd_step(gamma, delta, y, g, h, p)
        gamma, delta, y = floyd_step(gamma, delta, y, g, h, p)

        if x == y:
            return gamma - alpha, delta - beta


def rho_pollard_floyd(g: int, h: int, p: int, verbose=False) -> int:
    if verbose:
        print("g: {}, h: {}, p: {}".format(g, h, p))
    u, v = rho_floyd(g, h, p)
    # u  + x*v  = 0 mod p-1
    delta = gcd(v, p - 1)

    N_delta = (p - 1) // delta
    v_delta = v // delta
    u_delta = u // delta

    inv_v_delta = ZZ(v_delta).inverse_mod(N_delta)

    x_N_delta = (-u_delta * inv_v_delta) % N_delta

    if verbose:
        print("u: {}, v: {}, delta: {}, u_delta: {}, v_delta:{}, N_delta: {}, x_N_delta: {}".format(u, v, delta, u_delta, v_delta, N_delta, x_N_delta))

    if delta < 100:
        # Dans ce cas, on teste toutes les valeurs pour retrouver le quotient de x par N_delta
        for z in range(delta):
            dlog = z * N_delta + x_N_delta
            calc = exp_mod(g, dlog, p, verbose)
            if verbose:
                print("dlog: {}, calc: {}".format(dlog, calc))
            if calc == h:
                return dlog
        print("Error: could not find a z such that x = z * N_delta + x_N_delta is a solution")
        print("u: {}, v: {}, delta: {}, u_delta: {}, v_delta:{}, N_delta: {}, x_N_delta: {}".format(u, v, delta, u_delta, v_delta, N_delta, x_N_delta))
    else:
        # Dans ce cas, on fait un appel récursif avec g = g^(p-1)/delta et h = hg^-xdelta
        new_g = exp_mod(g, N_delta, p, verbose)
        new_h = h * exp(g, p - 1 - x_N_delta) % p
        new_p = N_delta + 1
        z = rho_pollard_floyd(new_g, new_h, new_p, verbose)
        return z * N_delta + x_N_delta
