import random

EXCUSES = [
    "Floating point emotions",
    "Quantum interference",
    "Cosmic rays",
    "Skill issue",
    "Math had a bad day",
    "Blame the compiler"
]

def random_error():
    return random.choice(EXCUSES)
