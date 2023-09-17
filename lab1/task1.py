from tkinter import ttk

from functions import simulate_event


class Task1:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        self.info_label = ttk.Label(self.frame, text='Insert event probability (from 0 to 1)')
        self.info_label.grid(row=0, column=0)

        self.probability_input = ttk.Entry(self.frame)
        self.probability_input.grid(row=1, column=0)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(row=2, column=0)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.calculate)
        self.submit_button.grid(row=3, column=0)

        self.result_label = ttk.Label(self.frame)
        self.result_label.grid(row=4, column=0)

    def draw(self):
        self.parent.add(self.frame, text='Task 1')

    def calculate(self):
        self.error_label.config(text='')
        self.result_label.config(text='')
        try:
            count = 1_000_000

            probability = float(self.probability_input.get())
            if probability > 1 or probability < 0:
                raise Exception('Probability should be from 0 to 1')

            success = 0
            for i in range(0, count):
                if simulate_event(probability):
                    success += 1

            result = success / count
            self.result_label.config(
                text=f'Result:\nP(A): {result}\nP(!A): {1 - result}')

        except ValueError:
            self.error_label.config(text='Invalid value')
        except Exception as e:
            self.error_label.config(text=str(e))
