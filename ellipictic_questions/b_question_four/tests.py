from sage.all import *
from ellipictic_questions.b_question_four.ss_generator import generate_ss


def test_ss(verbose=False):
    p = 313
    ss_curve = generate_ss(p, verbose)
    print("Found ", ss_curve)