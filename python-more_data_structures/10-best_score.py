#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    scoremax = 0
    if a_dictionary is None:
        return None
    if len(a_dictionary) > 0:
        for name, score in a_dictionary.items():
            if score > scoremax:
                scoremax = score
                best = name
    return best
