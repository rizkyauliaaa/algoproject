from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import *

class Experiment:
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
        self.index = 0

    def results(self):
        if self.age < 7:
            self.index = 0
            return "there is no data for this age"

        self.index = (4 * (int(self.t1) + int(self.t2) + int(self.t3)) - 200) / 10

        if self.age == 7 or self.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5

        if self.age == 9 or self.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5

        if self.age == 11 or self.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5

    def __str__(self):
        return (
            f"Age: {self.age} | "
            f"Test 1: {self.t1} | "
            f"Test 2: {self.t2} | "
            f"Test 3: {self.t3}"
        )


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        self.exp = exp

        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.workh_text = QLabel("Result: " + str(self.exp.results()))
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)