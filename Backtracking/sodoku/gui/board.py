# Sodoku Board

import tkinter as tk
from solver import Solver
from node import Node
import time


class Board:

    def __init__(self, board):
        """
            init sodoku board GUI
        """

        self.root = tk.Tk()
        self.is_solving = False
        self.root.title('Sodoku')
        self.root.resizable(False, False)
        self.board = board
        self.selected_node = None
        self.start = time.time()
        self.elapsed_time = tk.StringVar()
        self.board_frame = None
        self.timer_frame = None
        self.timer_value_label = None
        self.nodes = []
        self.render_ui()
        self.render_board()
        self.update_clock()
        self.solver = Solver()
        self.solver.register(self)
        self.root.mainloop()

    def render_ui(self):
        """
            render ui frames and labels
        """

        self.board_frame = tk.Frame(self.root)
        self.timer_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=0, padx=25, pady=25)
        self.timer_frame.grid(row=1, column=0)
        elapsed_time_label = tk.Label(self.timer_frame, text="Time:", padx=10, pady=10, font=("Courier", 20))
        self.timer_value_label = tk.Label(self.timer_frame, textvariable=self.elapsed_time, padx=10, pady=10, font=("Courier", 20))
        elapsed_time_label.grid(row=0, column=0)
        self.timer_value_label.grid(row=0, column=1)

    def render_board(self):
        """
            render sodoku board
        """

        for r in range(0, 9):
            for c in range(0, 9):
                node_val = " "
                is_initial_value = False
                index = self.get_one_d_node_index(r, c)
                if self.board[r][c] != 0:
                    node_val = self.board[r][c]
                    is_initial_value = True
                node = Node(self.board_frame, r, c, index, is_initial_value, node_val)
                node.label.grid(row=r, column=c)
                self.bind_events(node)
                self.nodes.append(node)

    def value_entered_event(self, event):
        """
            detect key press events
        """

        if self.selected_node is not None \
                and self.selected_node.is_initial_value\
                or self.is_solving:
            return
        value = None
        kp = repr(event.keysym)
        if kp == '\'1\'':
            value = 1
        elif kp == '\'2\'':
            value = 2
        elif kp == '\'3\'':
            value = 3
        elif kp == '\'4\'':
            value = 4
        elif kp == '\'5\'':
            value = 5
        elif kp == '\'6\'':
            value = 6
        elif kp == '\'7\'':
            value = 7
        elif kp == '\'8\'':
            value = 8
        elif kp == '\'9\'':
            value = 9
        if value is not None:
            self.enter_node_value(value)
            return
        if kp == '\'BackSpace\'':
            self.remove_node_value()
        if kp == '\'space\'':
            self.solve_board()

    def remove_node_value(self):
        """
            allow user to delete entered value
        """

        index = self.selected_node.index
        row = self.selected_node.row
        col = self.selected_node.col
        if not self.selected_node.is_initial_value:
            self.board[row][col] = 0
            self.nodes[index].value.set(' ')

    def enter_node_value(self, value):
        """
            enter a value in a cell
        """

        index = self.selected_node.index
        row = self.selected_node.row
        col = self.selected_node.col
        zero = [row, col]
        if self.solver.validate_entry(self.board, zero=zero, val=value, grid_size=3):
            self.board[row][col] = value
            self.nodes[index].value.set(value)

    def bind_events(self, node):
        """
            bind events to ui elements
        """

        self.root.bind("<Key>", self.value_entered_event)
        node.label.bind("<Key>", self.value_entered_event)
        node.label.bind("<Button-1>", self.node_selected)

    def update_selected_node(self, index):
        """
            update selected node config
        """

        for i, node in enumerate(self.nodes):
            if i == index:
                node.is_selected = True
                node.label.configure(bg='#B8E9FF')
                self.selected_node = node
            else:
                node.is_selected = False
                node.label.configure(bg='white')

    def node_selected(self, event):
        """
            focus on selected label
        """

        caller = event.widget
        caller.focus_set()
        row = caller.grid_info()['row']
        col = caller.grid_info()['column']
        index = self.get_one_d_node_index(row, col)
        self.update_selected_node(index)

    def get_one_d_node_index(self, row, col):
        """
            get ond d index
        """

        index = col + (row * len(self.board))
        return index

    def get_two_d_index(self, index):
        """
            get two d index
        """

        col = index % len(self.board)
        row = index // len(self.board)
        return row, col

    def solve_board(self):
        """
            solve board using backtracking algorithm
        """

        self.is_solving = True
        self.solver.solve_sodoku(self.board, self.nodes)

    def update_root(self, zero, val):
        """
            update node values with backtracking results
        """

        index = self.get_one_d_node_index(zero[0], zero[1])
        self.nodes[index].value.set(val)
        self.root.update()
        time.sleep(0.2)

    def update_board(self, index, value):
        """
            update node value on board
        """

        node = self.nodes[index]
        value = str(value)
        node.value.set(value)

    def update_clock(self):
        """
            update elapsed timer
        """

        self.elapsed_time.set(self.format_time(time.time() - self.start))
        self.root.after(1000, self.update_clock)

    @staticmethod
    def format_time(secs):
        """
            format seconds into (mins : seconds)
        """

        sec = round(secs % 60)
        minute = secs // 60
        t = " " + str(minute) + ":" + str(sec)
        return t
