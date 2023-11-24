from dlog_questions.a_one.exponentiation import exp


def miller_rabin(a: int, N: int, s: int, t: int) -> bool:
    """
    Implémente le test de Miller-Rabin pour un entier N de la forme N-1 = 2**s * t
    :param a: entier <= N pour lequel on vérifie qu'il est racine d'au moins un des X^(2^nt) - 1 mod N.
    :param N: entier à tester de la forme 2**s * t.
    :param s:
    :param t:
    :return: Faux si N est composé. Vrai si N n'a pas l'air composé.
    """
    z = exp(a, t) % N
    if z == 1 or z == N - 1:
        return True
    for _ in range(s):
        z = z ** 2 % N
        if z == N - 1:
            return True
    return False
