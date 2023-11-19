import random
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        self.hist_canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.hist_canvas_widget = self.hist_canvas.get_tk_widget()
        self.hist_canvas_widget.grid(columnspan=2, row=3, column=0)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(columnspan=2, row=5, column=0)

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
        for i in range(10_000):
            number = random.random()
            result.append(float(f.subs(y, number)))

        return result

    def calculate(self):
        try:
            a = int(self.left_boundary_input.get())
            b = int(self.right_boundary_input.get())

            x, y = sp.symbols("x y")
            f = sp.simplify(f'(x - {a}) / ({b} - {a})')
            self.fx_result_label.config(text=f'y = {f}')

            ksi = self._inverse_function(f, y, x)
            self.fy_inv_result_label.config(text=f'ksi = {ksi}')

            result = self._generate_numbers(ksi, y)
            self.ax.clear()
            self.ax.hist(result, color='blue')
            self.hist_canvas.draw()
        except ValueError:
            self.error_label.config(text='Invalid value')
        except Exception as e:
            self.error_label.config(text=str(e))
