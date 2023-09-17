import random


def simulate_event(probability: float):
    return random.choices([True, False], weights=[probability, 1 - probability])[0]


def simulate_complex_event(values: list, probabilities: list):
    return random.choices(values, weights=probabilities)[0]
