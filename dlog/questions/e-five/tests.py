import random

from dlog.questions.five.rho_floyd import rho_pollard_floyd
from dlog.questions.one.exponentiation import exp_mod
from dlog.questions.two.el_gamal import el_gamal


def test_q5(with_big_test=True, verbose=False):
    print("-----Test de la méthode rho de Pollard version Floyd avc 5 appels aléatoires-----")
    for i in range(5):
        bits = random.randint(10, 16)
        p, pk, sk = el_gamal(bits)

        dlog = rho_pollard_floyd(pk, sk, p)
        message = ""
        power = exp_mod(pk, dlog, p)
        if power == sk:
            message = "Succès pour p:{}, h:{} = {}^{}".format(p, pk, sk, dlog)
        else:
            message = "Erreur de la méthode pour p:{}, n:p^{} = {}".format(pk, dlog, power)
        print("[Test {}]: {}".format(i + 1, message))

    if with_big_test:
        print("\n\n")
        print("-----Test de la méthode rho de Pollard avec les exemples donnés-----")
        p, g, h = 10000000259, 4, 7562435736
        print("Exemple 1.  p: {}, g: {}, h: {}".format(p, g, h))
        dlog = rho_pollard_floyd(g, h, p, verbose)
        power = exp_mod(g, dlog, p)
        if power == h:
            print("L'algorithme a réussi et a trouvé h = {}^{}".format(g, dlog))
        else:
            print("L'algorithme a échoué et trouvé h = {}^{} != {}".format(g, dlog, power))

            p, g, h = 1000000000005719, 121, 383002468056629
            print("Exemple 2.  p: {}, g: {}, h: {}".format(p, g, h))
            dlog = rho_pollard_floyd(g, h, p, verbose)
            power = exp_mod(g, dlog, p)
            if power == h:
                print("L'algorithme a trouvé h = {}^{}".format(g, dlog))
            else:
                print("L'algorithme a échoué et trouvé h = {}^{}".format(g, dlog))
