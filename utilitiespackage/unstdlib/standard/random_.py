import logging
import random as _random


def set_random():
    try:
        random = _random.SystemRandom()
    except NotImplementedError:  # pragma: no cover
        log.warn("random.SystemRandom() is not available. Using random.Random() " "instead, this means that things will be less random.")
        random = _random.Random()
    globals()["random"] = random
    return {"random": random}


set_random()
