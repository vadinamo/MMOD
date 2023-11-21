import random
import sympy as sp
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import *


class Task1:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        left_boundary_label = ttk.Label(self.frame, text='Left boundary')
        left_boundary_label.grid(row=0, column=0)

        self.left_boundary_input = ttk.Entry(self.frame)
        self.left_boundary_input.grid(row=1, column=0)

        right_boundary_label = ttk.Label(self.frame, text='Right boundary')
        right_boundary_label.grid(row=0, column=1)

        self.right_boundary_input = ttk.Entry(self.frame)
        self.right_boundary_input.grid(row=1, column=1)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        self.submit_button.grid(columnspan=2, row=2, column=0)

        self.result_frame = ttk.Frame(self.frame)
        self.result_frame.grid(columnspan=2, row=3, column=0)

        fx_label = ttk.Label(self.result_frame, text='f(x) function: ')
        fx_label.grid(row=0, column=0)

        self.fx_result_label = ttk.Label(self.result_frame)
        self.fx_result_label.grid(row=0, column=1)

        fy_inv_label = ttk.Label(self.result_frame, text='f^-1(y) function: ')
        fy_inv_label.grid(row=1, column=0)

        self.fy_inv_result_label = ttk.Label(self.result_frame)
        self.fy_inv_result_label.grid(row=1, column=1)

        hist_label = ttk.Label(self.result_frame, text='Result values histogram:')
        hist_label.grid(columnspan=2, row=2, column=0)

        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(6, 4)
        self.hist_canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.hist_canvas_widget = self.hist_canvas.get_tk_widget()
        self.hist_canvas_widget.grid(columnspan=2, row=3, column=0)

        result_table_frame = ttk.Frame(self.result_frame)
        result_table_frame.grid(columnspan=2, row=4, column=0)

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
        self.error_label.grid(columnspan=2, row=4, column=0)

    def draw(self):
        self.parent.add(self.frame, text='Task 1')

    @staticmethod
    def _inverse_function(f, y, x):
        equation = sp.Eq(y, f)
        f_inv = sp.solve(equation, x)

        for f_inv_elem in f_inv:
            if f_inv_elem.subs(y, 1) > 0:
                return f_inv_elem

    @staticmethod
    def _generate_numbers(f, y):
        result = []
        for i in range(iterations):
            number = random.random()
            result.append(float(f.subs(y, number)))

        return result

    @staticmethod
    def _get_theoretical_math_expectation(f, x, a, b):
        return float(sp.integrate(x * f, (x, a, b)))

    @staticmethod
    def _get_theoretical_dispersion(f, x, a, b):
        return float(sp.integrate(x ** 2 * f, (x, a, b))) - Task1._get_theoretical_math_expectation(f, x, a, b) ** 2

    def calculate(self):
        try:
            a = int(self.left_boundary_input.get())
            b = int(self.right_boundary_input.get())

            if a > b:
                raise Exception("Left boundary should be lower than right")

            x, y = sp.symbols("x y")
            f = sp.simplify(f'(x - {a}) / ({b} - {a})')
            self.fx_result_label.config(text=f'y = {f}')

            ksi = self._inverse_function(f, y, x)
            self.fy_inv_result_label.config(text=f'ksi = {ksi}')

            result = self._generate_numbers(ksi, y)
            self.ax.clear()
            self.ax.hist(result, color='blue')
            self.hist_canvas.draw()

            df = sp.diff(f, x)

            self.math_expectation_theoretical_label.config(text=self._get_theoretical_math_expectation(df, x, a, b))
            self.math_expectation_practical_label.config(text=get_practical_math_expectation(result))

            self.dispersion_theoretical_label.config(text=self._get_theoretical_dispersion(df, x, a, b))
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
