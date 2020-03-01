# Sodoku Cell Node

import tkinter as tk


class Node:

    def __init__(self, parent, row, col, index, is_initial_value=False, value=None):
        self.value = tk.StringVar()
        self.value.set(value)
        self.is_initial_value = is_initial_value
        self.is_selected = False
        self.label = self.visual_node(parent)
        self.row = row
        self.col = col
        self.index = index

    def visual_node(self, parent):
        # value_text = " " if self.value == 0 else str(self.value)
        label = tk.Label(parent,
                         textvariable=str(self.value),
                         padx=15,
                         pady=10,
                         borderwidth=2,
                         relief='solid',
                         highlightbackground='white',
                         highlightcolor="white",
                         highlightthickness=0,
                         activebackground="white",
                         activeforeground="white",
                         font=("Courier", 30),
                         bg='white')
        return label
