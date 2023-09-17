from tkinter import ttk

from functions import simulate_complex_event, create_complex_output


class Task4:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        self.info_label = ttk.Label(self.frame, text='Insert probabilities separated by ","')
        self.info_label.grid(row=0, column=0)

        self.probabilities_input = ttk.Entry(self.frame)
        self.probabilities_input.grid(row=1, column=0)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(row=2, column=0)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        self.submit_button.grid(row=3, column=0)

        self.result_label = ttk.Label(self.frame)
        self.result_label.grid(row=4, column=0)

    def draw(self):
        self.parent.add(self.frame, text='Task 4')

    def calculate(self):
        self.error_label.config(text='')
        self.result_label.config(text='')
        try:
            count = 1_000_000

            probabilities = [float(x) for x in self.probabilities_input.get().replace(' ', '').split(',')]
            if any(p < 0 or p > 1 for p in probabilities):
                raise Exception("Probability values should be between 0 and 1")
            if sum(probabilities) != 1:
                raise Exception("Sum of probabilities must be 1")

            values = [i for i in range(len(probabilities))]
            result = [0 for _ in range(len(probabilities))]
            for i in range(count):
                result[int(simulate_complex_event(values, probabilities))] += 1

            self.result_label.config(text=create_complex_output(probabilities, result, count))

        except ValueError:
            self.error_label.config(text='Invalid values')
        except Exception as e:
            self.error_label.config(text=str(e))
