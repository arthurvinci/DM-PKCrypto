from sage.all import *
from dlog.questions.one.exponentiation import exp
from dlog.questions.one.generation_premiers import gen_prime
import random


def test_exp():
    print("-----Test de l'exponentiation avec 10 appels aléatoires-----")
    for i in range(10):
        r = random.randint(100, 10000)
        n = random.randint(100, 1000)
        r1 = exp(r, n)
        r2 = r ** n
        message = ""
        if r1 != r2:
            message = "Erreur d'exponentiation pour x:{} et n:{}".format(r, n)
        else:
            message = "Succès pour x:{}, n:{}".format(r, n)
        print("[Test {}]: {}".format(i + 1, message))


def test_gen_prime():
    print("-----Test de la génération de premiers avec 5 appels aléatoires-----")
    for i in range(5):
        r = random.randint(10, 20)
        p = gen_prime(r)
        l = list(factor(p))
        message = ""
        if len(l) > 1:
            message = "Erreur avec l = {} bits : {} = {}".format(r, p, l)
        else:
            message = "Succès pour l = {} bits : {}".format(r, p)
        print("[Test {}]: {}".format(i + 1, message))


def test_q1():
    test_exp()
    print("\n\n")
    test_gen_prime()
