def naive_dlog(gen: int, h: int, p: int, verbose=False) -> int:
    if verbose:
        print("Computing naive dlog for p:{}, g:{}, h:{}".format(p, gen, h))
    g = gen
    a = 1
    while g != h:
        g = (g * gen) % p
        a += 1
        a = a % p
        if verbose:
            print(g, a)
    return a
