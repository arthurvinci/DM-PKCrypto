from sage.all import *

from ellipictic_questions.b_question_four.ss_test import is_supersingular


def generate_ss(p: int, verbose=False):
    F = GF(p).algebraic_closure()
    Fp2 = GF((p, 2))
    while True:
        j = Fp2.random_element()
        if is_supersingular(j, p, F, Fp2, verbose):
            return j


def generate_ordinary(p: int, verbose=False):
    F = GF(p).algebraic_closure()
    Fp2 = GF((p, 2))
    while True:
        j = Fp2.random_element()
        if not is_supersingular(j, p, F, Fp2, verbose):
            return j
