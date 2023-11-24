from dlog_questions.a_one.tests import test_q1
from dlog_questions.c_three.tests import test_q3
from dlog_questions.d_four.tests import test_q4
from dlog_questions.e_five.tests import test_q5
from ellipictic_questions.b_question_four.tests import test_ss


def test_dlog(verbose=False):
    test_q1()
    print("\n\n")
    test_q3(verbose)
    print("\n\n")
    test_q4(verbose)
    print("\n\n")
    test_q5(verbose)


def test_elliptic(verbose=False):
    test_ss(verbose)


#test_elliptic(True)
#test_dlog()