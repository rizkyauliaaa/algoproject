from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0)

        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_timer = QLabel("00:00:00")

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)

        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_name)
        self.layout.addWidget(self.line_name)
        self.layout.addWidget(self.text_age)
        self.layout.addWidget(self.line_age)
        self.layout.addWidget(self.btn_test1)
        self.layout.addWidget(self.btn_test2)
        self.layout.addWidget(self.btn_test3)
        self.layout.addWidget(self.text_timer)
        self.layout.addWidget(self.line_test1)
        self.layout.addWidget(self.line_test2)
        self.layout.addWidget(self.line_test3)
        self.layout.addWidget(self.btn_next)

        self.setLayout(self.layout)

    def next_click(self):
        self.hide()

        self.exp = Experiment(
            int(self.line_age.text()),
            self.line_test1.text(),
            self.line_test2.text(),
            self.line_test3.text()
        )

        self.fw = FinalWin(self.exp)

    def timer_test(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer_final(self):
        global time
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString("hh:mm:ss"))

        if int(self.time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(self.time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)