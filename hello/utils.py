import random

adjectives = [
    "scattered",
    "madly",
    "greedy",
    "bustling",
    "famous",
    "wholesale",
    "innate",
    "shrill",
    "asymptotic",
    "special",
    "deranged",
    "zesty",
]

nouns = [
    "pies",
    "bars",
    "lines",
    "curves",
    "slices",
    "graphs",
    "charts",
    "plots",
]

def game_name_generator():
    return random.choice(adjectives) + "-" + random.choice(nouns)