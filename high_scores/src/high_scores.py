high_scores = [1, 2, 3, 4, 5]


import pdb


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    # top_3 = []
    # pdb.set_trace()
    scores.sort()
    scores.reverse()
    if len(scores) < 3:
        top_3 = len(scores)

    return scores[:3]


def high_to_low(scores):
    scores.sort(reverse=True)
    new_list = scores
    # new_list.reverse()
    # return scores
    return new_list
