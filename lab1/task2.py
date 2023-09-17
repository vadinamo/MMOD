from tkinter import ttk

from functions import simulate_event


class Task2:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        self.info_label = ttk.Label(self.frame, text='Insert events probabilities separated by ","')
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
        self.parent.add(self.frame, text='Task 2')

    def calculate(self):
        self.error_label.config(text='')
        try:
            probabilities = [float(x) for x in self.probabilities_input.get().replace(' ', '').split(',')]
            if any(p < 0 or p > 1 for p in probabilities):
                raise Exception("Probability values should be between 0 and 1")

            output = []
            for probability in probabilities:
                print('asd')
                output.append([probability, simulate_event(probability)])

            self.result_label.config(
                text='\n'.join([' '.join(map(str, item)) for item in output]))

        except ValueError:
            self.error_label.config(text='Invalid values')
        except Exception as e:
            self.error_label.config(text=str(e))
