from tkinter import ttk

from functions import simulate_complex_event, create_complex_output


class Task3:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        self.a_info_label = ttk.Label(self.frame, text='Insert P(A) probability')
        self.a_info_label.grid(row=0, column=0)

        self.a_probability_input = ttk.Entry(self.frame)
        self.a_probability_input.grid(row=1, column=0)

        self.ba_info_label = ttk.Label(self.frame, text='Insert P(B|A) probability')
        self.ba_info_label.grid(row=2, column=0)

        self.ba_probability_input = ttk.Entry(self.frame)
        self.ba_probability_input.grid(row=3, column=0)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(row=4, column=0)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        self.submit_button.grid(row=5, column=0)

        self.result_label = ttk.Label(self.frame)
        self.result_label.grid(row=6, column=0)

    def draw(self):
        self.parent.add(self.frame, text='Task 3')

    def calculate(self):
        self.error_label.config(text='')
        self.error_label.config(text='')
        try:
            count = 1_000_000

            a = float(self.a_probability_input.get())
            ba = float(self.ba_probability_input.get())

            a_b = round(a * ba, 4)
            a_not_b = round(a * (1 - ba), 4)
            not_a_b = round((1 - a) * (1 - ba), 4)
            not_a_not_b = round(1 - a_b - a_not_b - not_a_b, 4)

            probabilities = [a_b, a_not_b, not_a_b, not_a_not_b]

            result = [0, 0, 0, 0]
            for i in range(count):
                result[int(simulate_complex_event([0, 1, 2, 3], probabilities))] += 1

            self.result_label.config(
                text=create_complex_output(probabilities, result, count))

        except ValueError:
            self.error_label.config(text='Invalid values')
        except Exception as e:
            self.error_label.config(text=str(e))
