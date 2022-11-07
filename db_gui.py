import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk() # Create new window to house all the interface.
    root.title("Blood Donor Database window")
    root.geometry("600x300") #makes the initial size of the window
    ttk.Label(root, text="Blood Donor Database").grid(column = 0, row = 0) # this shriks the window so this fits.
    ttk.Label(root, text="Name").grid(column = 0, row = 1)
    ttk.Entry(root).grid(column = 1, row = 1, columnspan=2)


    root.mainloop() # this starts the interface.


if __name__ == '__main__':
    main_window()