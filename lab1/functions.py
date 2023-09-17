import random


def simulate_event(probability: float):
    return random.choices([True, False], weights=[probability, 1 - probability])[0]
