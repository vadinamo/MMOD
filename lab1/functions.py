import random


def simulate_event(probability: float):
    return random.choices([True, False], weights=[probability, 1 - probability])[0]


def simulate_complex_event(values: list, probabilities: list):
    return random.choices(values, weights=probabilities)[0]


def create_complex_output(probabilities, result, count):
    output = []
    for i in range(len(probabilities)):
        output.append([probabilities[i], result[i] / count])

    return '\n'.join([' '.join(map(str, item)) for item in output])
