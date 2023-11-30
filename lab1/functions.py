import random


# class Random:
#     def __init__(self, A):
#         self.A = A
#         self.K = 16807
#         self.M = 2 ** 31 - 1
#
#     def next(self):
#         self.A = (self.A * self.K) % self.M
#         return self.A / self.M
#
#
# r = Random(111)

def generate_random(values, weights):
    if len(weights) != len(values):
        raise Exception('Weights count must be equal count of values')

    r = random.uniform(0, 1)

    s = 0
    for i in range(len(weights)):
        s += weights[i]
        if r <= s:
            return values[i]


def simulate_event(probability: float):
    return generate_random([True, False], weights=[probability, 1 - probability])


def simulate_complex_event(values: list, probabilities: list):
    return generate_random(values, weights=probabilities)


def create_complex_output(probabilities, result, count):
    output = []
    for i in range(len(probabilities)):
        output.append([probabilities[i], result[i] / count])

    return '\n'.join([' '.join(map(str, item)) for item in output])
