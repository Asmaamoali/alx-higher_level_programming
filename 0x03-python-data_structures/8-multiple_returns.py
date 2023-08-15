#!/usr/bin/python3
#8-multiple_returns.py
def multiple_returns(sentence):
    """Multiple returns"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

