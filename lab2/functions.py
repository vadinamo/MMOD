import numpy as np
from scipy.stats import chi

iterations = 10_000


def get_practical_math_expectation(values):
    return sum(values) / len(values)


def get_practical_dispersion(values):
    s = 0
    math_expression = get_practical_math_expectation(values)
    for element in values:
        s += (element - math_expression) ** 2
    return s / (len(values) - 1)


def get_math_expectation_confidence_interval(result):
    t = 1.96
    math_exp = get_practical_math_expectation(result)
    dispersion = get_practical_dispersion(result)
    delta = t * (dispersion ** 0.5) / (iterations ** 0.5)
    return math_exp - delta, math_exp + delta


def get_dispersion_confidence_interval(result, confidence_level):
    standard_deviation = np.sqrt(get_practical_dispersion(result))
    alpha1 = (1 - confidence_level) / 2
    alpha2 = (1 + confidence_level) / 2
    chi1 = chi.ppf(alpha1, iterations - 1)
    chi2 = chi.ppf(alpha2, iterations - 1)
    return (iterations - 1) * (standard_deviation ** 2) / (chi2 ** 2), (iterations - 1) * (
            standard_deviation ** 2) / (chi1 ** 2)
