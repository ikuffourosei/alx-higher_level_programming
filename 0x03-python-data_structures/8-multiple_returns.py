#!/usr/bin/python3


def multiple_returns(sentence):
    s = len(sentence)
    if sentence == "":
        result = (0, None)
    result = (s, sentence[0])
    return result
