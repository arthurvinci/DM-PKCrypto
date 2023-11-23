from sage.all import *

from dlog.questions.one.exponentiation import exp_mod
from dlog.questions.one.generation_premiers import gen_prime
import random


def gen(p: int) -> int:
    factors = list(ZZ(p-1).factor())
    for i in range(2, p):
        all_not_one = True
        for prime_factor in factors:
            factor, _ = prime_factor
            factor = int(factor)
            power = exp_mod(i, (p-1)//factor, p)
            if power == 1:
                all_not_one = False
                break
        if all_not_one:
            return i

def el_gamal(nb_bits: int) -> (int, int, int):
    """
    Implémente le protocole de génération de clés pour El Gamal.
    :param nb_bits: nombre de bits des clés.
    :return: un couple (clé publique, clé privée)
    """
    p = gen_prime(nb_bits)
    a = random.randint(2, p - 2)
    pk = gen(p)
    sk = exp_mod(pk, a, p)

    return p, pk, sk
