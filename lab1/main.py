import tkinter as tk
from tkinter import ttk

from tasks.task1 import Task1
from tasks.task2 import Task2
from tasks.task3 import Task3
from tasks.task4 import Task4
from tasks.task_additional import AdditionalTask


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
    task4 = Task4(tab_control)
    task4.draw()
    additional_task = AdditionalTask(tab_control)
    additional_task.draw()

    tab_control.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == "__main__":
    main()
