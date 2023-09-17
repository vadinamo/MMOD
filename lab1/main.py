import tkinter as tk
from tkinter import ttk

from task1 import Task1
from task2 import Task2
from task3 import Task3


def main():
    root = tk.Tk()
    root.title("Lab 1")

    tab_control = ttk.Notebook(root)

    task1 = Task1(tab_control)
    task1.draw()
    task2 = Task2(tab_control)
    task2.draw()
    task3 = Task3(tab_control)
    task3.draw()

    tab_control.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == "__main__":
    main()
