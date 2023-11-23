import random
from dlog.questions.one.exponentiation import exp
from dlog.questions.one.miller_rabin import miller_rabin

first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
                347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def divisible_by_small_prime(N: int) -> bool:
    """
    Vérifie si un entier `N` est divisible par l'un des 100 premiers premiers.
    :param N: entier `N` à tester
    :return: renvoie si `N` est divisible par l'un des 100 premiers premiers
    """
    for p in first_primes:
        if N % p == 0:
            return True
    return False


def small_prime(nb_bits: int) -> int:
    primes_with_bits = []
    smallest_prime = 2 ** nb_bits
    biggest_prime = 2 ** (nb_bits+1) - 1

    for p in first_primes:
        if smallest_prime <= p <= biggest_prime:
            primes_with_bits.append(p)
    amount = len(primes_with_bits)
    i = random.randrange(0, amount-1)
    return primes_with_bits[i]


def gen_prime(nb_bits: int) -> int:
    """
    Génère un entier premier de `nb_bits` bits sous l'hypothèse de Riemann généralisée.
    :param nb_bits:
    :return:
    """
    if nb_bits <= 9:
        return small_prime(nb_bits)

    range_min = exp(2, nb_bits)
    range_max = exp(2, nb_bits + 1)
    while True:
        N = random.randrange(range_min, range_max)
        if divisible_by_small_prime(N):
            continue
        s = 0
        t = N - 1
        while t % 2 == 0 and t > 1:
            s += 1
            t = t // 2

        all_true = True

        for a in range(1, 2 * nb_bits ** 2 + 1):
            if not miller_rabin(a, N, s, t):
                all_true = False
                break

        if all_true:
            return N
