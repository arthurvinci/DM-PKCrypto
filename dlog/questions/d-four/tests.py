import random

from dlog.questions.four.pohlig_hellman import pohlig_hellman
from dlog.questions.one.exponentiation import exp, exp_mod
from dlog.questions.two.el_gamal import el_gamal


def test_q4(with_big_test=True, verbose=False):
    print("-----Test de Pohlig-Hellman avec 5 appels aléatoires-----")
    for i in range(5):
        bits = random.randint(10, 16)
        p, pk, sk = el_gamal(bits)

        if verbose:
            print("Test with {} bits, p : {}, pk: {}, sk: {}".format(bits, p, pk, sk))

        dlog = pohlig_hellman(p, pk, sk)
        message = ""
        power = exp(pk, dlog) % p
        if power == sk:
            message = "Succès pour p:{}, h:{} = {}^{}".format(p, pk, sk, dlog)
        else:
            message = "Erreur de la méthode pour p:{}, n:p^{} = {}".format(pk, dlog, power)
        print("[Test {}]: {}".format(i + 1, message))

    if with_big_test:
        print("\n\n")
        print("-----Test de Pohlig-Hellman avec l'exemple donné-----")
        p, g, h = 13827821670227353601, 3, 10780909174164501009
        print("Exemple 1.  p: {}, g: {}, h: {}".format(p, g, h))
        dlog = pohlig_hellman(p, g, h, verbose)
        power = exp_mod(g, dlog, p, verbose) % p
        if power == h:
            print("L'algorithme a réussi et a trouvé h = {}^{}".format(g, dlog))
        else:
            print("L'algorithme a échoué et trouvé h = {}^{} != {}".format(g, dlog, power))

