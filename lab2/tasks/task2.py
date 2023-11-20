import random
import math
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import *


class Task2:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        n_input_label = ttk.Label(self.frame, text='n:')
        n_input_label.grid(row=0, column=0)

        self.n_input = ttk.Entry(self.frame)
        self.n_input.grid(row=1, column=0)

        p_input_label = ttk.Label(self.frame, text='p:')
        p_input_label.grid(row=0, column=1)

        self.p_input = ttk.Entry(self.frame)
        self.p_input.grid(row=1, column=1)

        x_input_label = ttk.Label(self.frame, text='x:')
        x_input_label.grid(row=0, column=2)

        self.x_input = ttk.Entry(self.frame)
        self.x_input.grid(row=1, column=2)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        self.submit_button.grid(columnspan=3, row=2, column=0)

        self.result_frame = ttk.Frame(self.frame)
        self.result_frame.grid(columnspan=3, row=3, column=0)

        hist_label = ttk.Label(self.result_frame, text='Result values histogram:')
        hist_label.grid(row=0, column=0)

        self.fig, self.ax = plt.subplots()
        self.hist_canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.hist_canvas_widget = self.hist_canvas.get_tk_widget()
        self.hist_canvas_widget.grid(row=1, column=0)

        result_table_frame = ttk.Frame(self.result_frame)
        result_table_frame.grid(row=2, column=0)

        confidence_interval_math_expectation_label = ttk.Label(result_table_frame,
                                                               text='Confidence interval (Math expectation)')
        confidence_interval_math_expectation_label.grid(row=0, column=0)

        self.confidence_interval_math_expectation_left_label = ttk.Label(result_table_frame)
        self.confidence_interval_math_expectation_left_label.grid(row=0, column=1)

        self.confidence_interval_math_expectation_right_label = ttk.Label(result_table_frame)
        self.confidence_interval_math_expectation_right_label.grid(row=0, column=2)

        confidence_interval_dispersion_label = ttk.Label(result_table_frame, text='Confidence interval (Dispersion)')
        confidence_interval_dispersion_label.grid(row=1, column=0)

        self.confidence_interval_dispersion_left_label = ttk.Label(result_table_frame)
        self.confidence_interval_dispersion_left_label.grid(row=1, column=1)

        self.confidence_interval_dispersion_right_label = ttk.Label(result_table_frame)
        self.confidence_interval_dispersion_right_label.grid(row=1, column=2)

        theoretical_label = ttk.Label(result_table_frame, text='Theoretical')
        theoretical_label.grid(row=2, column=1)

        practical_label = ttk.Label(result_table_frame, text='Practical')
        practical_label.grid(row=2, column=2)

        math_expectation_label = ttk.Label(result_table_frame, text='Mathematical expectation')
        math_expectation_label.grid(row=3, column=0)

        self.math_expectation_theoretical_label = ttk.Label(result_table_frame)
        self.math_expectation_theoretical_label.grid(row=3, column=1)

        self.math_expectation_practical_label = ttk.Label(result_table_frame)
        self.math_expectation_practical_label.grid(row=3, column=2)

        dispersion_label = ttk.Label(result_table_frame, text='Dispersion')
        dispersion_label.grid(row=4, column=0)

        self.dispersion_theoretical_label = ttk.Label(result_table_frame)
        self.dispersion_theoretical_label.grid(row=4, column=1)

        self.dispersion_practical_label = ttk.Label(result_table_frame)
        self.dispersion_practical_label.grid(row=4, column=2)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(columnspan=3, row=4, column=0)

    def draw(self):
        self.parent.add(self.frame, text='Task 2')

    @staticmethod
    def probability_function(n, x, p):
        if x > n:
            return 0
        return math.comb(n - 1, n - x) * (p ** x) * ((1 - p) ** (n - x))

    @staticmethod
    def pascal_distribution(x, p):
        result = []
        for _ in range(iterations):
            result.append(sum(Task2.geometric_distribution(p) for _ in range(x)))

        return result

    @staticmethod
    def geometric_distribution(p):
        return math.ceil(math.log10(random.random()) / math.log10(1 - p))

    @staticmethod
    def _get_theoretical_math_expectation(x, p):
        return x / p

    @staticmethod
    def _get_theoretical_dispersion(x, p):
        return x * (1 - p) / (p ** 2)

    def calculate(self):
        try:  # 50 0.4 20
            n = int(self.n_input.get())
            p = float(self.p_input.get())
            x = int(self.x_input.get())

            if n < 1:
                raise Exception('n should be >= 1')

            if p < 0 or p > 1:
                raise Exception('p should be between 0 and 1')

            if x < 0 or x > n:
                raise Exception('x should be between 0 and n value')

            r = list(range(1, n))
            values = [Task2.probability_function(i, x, p) for i in r]

            self.ax.clear()
            self.ax.plot(r, values, color='blue')
            self.hist_canvas.draw()

            result = self.pascal_distribution(x, p)
            self.math_expectation_theoretical_label.config(text=self._get_theoretical_math_expectation(x, p))
            self.math_expectation_practical_label.config(text=get_practical_math_expectation(result))

            self.dispersion_theoretical_label.config(text=self._get_theoretical_dispersion(x, p))
            self.dispersion_practical_label.config(text=get_practical_dispersion(result))

            math_expectation_confidence_interval = get_math_expectation_confidence_interval(result)
            self.confidence_interval_math_expectation_left_label.config(text=math_expectation_confidence_interval[0])
            self.confidence_interval_math_expectation_right_label.config(text=math_expectation_confidence_interval[1])

            dispersion_confidence_interval = get_dispersion_confidence_interval(result, 0.95)
            self.confidence_interval_dispersion_left_label.config(text=dispersion_confidence_interval[0])
            self.confidence_interval_dispersion_right_label.config(text=dispersion_confidence_interval[1])
        except ValueError:
            self.error_label.config(text='Invalid value')
        except Exception as e:
            self.error_label.config(text=str(e))
