from sage.all import *

from dlog_questions.a_one.exponentiation import exp_mod


def baby_step_giant_step(gen: int, h: int, p: int, verbose=False, s=3) -> int:
    if verbose:
        print("Running baby step giant step for gen:{}, h:{}, p:{}, s:{}".format(gen, h, p, s))
    baby_steps = [gen ** i % p for i in range(0, s)]
    inv_gen = ZZ(gen).inverse_mod(p)
    inv_gen_s = exp_mod(inv_gen, s, p)
    step = 0
    prev_step = h
    while True:
        for i in range(len(baby_steps)):
            if prev_step == baby_steps[i]:
                if verbose:
                    print("Collision pour step = {}, h_step = {}, i: {}".format(step, prev_step, i))
                return (step * s + i) % p

        prev_step = (inv_gen_s * prev_step) % p
        step += 1
