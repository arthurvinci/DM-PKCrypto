import random

from dlog.questions.one.exponentiation import exp_mod
from dlog.questions.three.naive_dlog import naive_dlog
from dlog.questions.two.el_gamal import el_gamal


def test_q3():
    print("-----Test du log discret naïf avec 5 appels aléatoires-----")
    for i in range(5):
        bits = random.randint(10, 20)
        p, pk, sk = el_gamal(bits)
        dlog = naive_dlog(pk, sk, p)
        message = ""
        power = exp_mod(pk, dlog, p)
        if power == sk:
            message = "Succès pour p:{}, n:p^{}".format(pk, dlog)
        else:
            message = "Erreur de log pour p:{}, n:p^{}".format(pk, dlog)
        print("[Test {}]: {}".format(i + 1, message))
