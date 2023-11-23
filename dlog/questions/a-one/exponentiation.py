def exp(x: int, n: int, verbose=False) -> int:
    """
    Implémente l'exponentiation rapide bonaire.
    :param verbose:
    :param x: nombre à exponentier
    :param n: exposant.
    :return: x**n
    """
    if verbose:
        print("Call for x: {}, n:{}".format(x, n))
    if n == 0:
        if verbose:
            print("Returning 1")
        return 1
    z = exp(x, n // 2, verbose) ** 2
    if verbose:
        print("End of recursive call for x: {}, n:{}".format(x, n))
    if n % 2 == 1:
        z = x * z
    return z


def exp_mod(x: int, n: int, mod: int, verbose=False) -> int:
    if verbose:
        print("Call for x: {}, n:{}, mod:{}".format(x, n, mod))
    if n == 0:
        return 1
    z = exp_mod(x, n // 2, mod, verbose)
    z = z**2 % mod
    if verbose:
        print("End of recursive call for x: {}, n:{} z:{} mod: {}".format(x, n, z, mod))
    if n % 2 == 1:
        z = x * z % mod
    return z
