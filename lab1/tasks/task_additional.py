from tkinter import ttk

from functions import simulate_complex_event


class AdditionalTask:
    def __init__(self, parent: ttk.Notebook):
        self.parent = parent

        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=1, column=0)

        games_info_label = ttk.Label(self.frame, text='Current games')
        games_info_label.grid(row=0, column=0)

        self.games_label = ttk.Label(self.frame)
        self.games_label.grid(row=1, column=0)

        self.roll_button = ttk.Button(self.frame, text="Roll", command=self.roll)
        self.roll_button.grid(row=2, column=0)

        self.roll_result = ttk.Label(self.frame)
        self.roll_result.grid(row=3, column=0)

        donation_label = ttk.Label(self.frame, text='Make donation')
        donation_label.grid(row=0, column=1)

        donation_frame = ttk.Frame(self.frame)
        donation_frame.grid(row=1, column=1)

        game_input_label = ttk.Label(donation_frame, text='Game name')
        game_input_label.grid(row=0, column=0)

        self.game_input = ttk.Entry(donation_frame)
        self.game_input.grid(row=0, column=1)

        donation_amount_label = ttk.Label(donation_frame, text='Amount')
        donation_amount_label.grid(row=1, column=0)

        self.donation_amount_input = ttk.Entry(donation_frame)
        self.donation_amount_input.grid(row=1, column=1)

        self.donate_button = ttk.Button(self.frame, text="Donate", command=self.make_donation)
        self.donate_button.grid(row=2, column=1)

        self.error_label = ttk.Label(self.frame)
        self.error_label.grid(row=3, column=1)

        self.games = {}

    def draw(self):
        self.parent.add(self.frame, text='Fortune\'s wheel')

    def update(self):
        self.error_label.config(text='')
        self.games_label.config(text='\n'.join([f'{key}: {value}' for key, value in self.games.items()]))

    def roll(self):
        if len(self.games) < 2:
            self.error_label.config(text='There is less than 2 games...')
            return

        total_sum = sum(self.games.values())

        values = []
        probabilities = []
        for key, value in self.games.items():
            values.append(key)
            probabilities.append(value / total_sum)

        result = simulate_complex_event(values, probabilities)
        self.roll_result.config(text=f'Winner: {result} with amount: {self.games[result]}! Congratulations!')

        self.games.clear()
        self.update()

    def make_donation(self):
        try:
            amount = float(self.donation_amount_input.get())
            game_name = self.game_input.get()
            if game_name.replace(' ', '').replace('/t', '') == '':
                raise Exception('Empty game name')

            if game_name in self.games:
                self.games[game_name] += amount
            else:
                self.games[game_name] = amount

            self.update()
        except ValueError:
            self.error_label.config(text='Invalid values')
        except Exception as e:
            self.error_label.config(text=str(e))
