from sage.all import *
from ellipictic_questions.a_question_two.paths import neighbours, nb_path


def is_supersingular(j, p, F, Fp2, verbose=False):
    neighs = neighbours(j, F)
    paths = []
    if verbose:
        print("Création de chemins de taille: ", p//12 + 3)
    for i in range(2):
        paths.append(nb_path(j, neighs[i], p // 12 + 3, F, verbose))

    for j in range(p // 12 + 4):
        for i in range(2):
            if paths[i][j] not in Fp2:
                return False

    return True
