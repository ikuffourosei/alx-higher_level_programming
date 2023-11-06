#!/usr/bin/python3


def multiple_returns(sentence):
    s = len(sentence)
    if sentence == "":
        sentence[0] = None
    result = (s, sentence[:1])
    return result
