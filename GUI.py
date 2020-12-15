import PySimpleGUI as sg
from sys import argv, exit
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
from b64_images import *

sg.theme('DarkBlue16')  # theme


titlebar = [[sg.Button("", image_data=b64_img,                   # exit button
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       border_width=0, key='Exit', tooltip="Exit the program")]]


win = [[sg.Column(titlebar, justification="r")],                # creating the window layout
       [sg.Text("Press the button to start!", font="rockwell 20", justification="center")],
       [sg.Button("Start!", font="dubai 20", border_width=0, tooltip="Start", size=(9, 1), pad=(0,50), key="start")],
       [sg.Text("Status", font="dubai 20", key="status", size=(25, 1), justification="c", enable_events=True)]]


trWin = sg.Window("", win,
                  keep_on_top=True,
                  no_titlebar=True,
                  size=(450, 300),              # creating the window
                  alpha_channel=0.7,
                  grab_anywhere=True,
                  element_justification="c")


class MyWidget(QtWidgets.QWidget):                              # snipping tool
    def __init__(self):
        super().__init__()
        root = tk.Tk("asdas")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        print('Take a snip')
        self.show()
        root.destroy()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('image.png')


def takeSnip():
    app = QtWidgets.QApplication(argv)
    window = MyWidget()
    window.show()                               # function to start the snipping tool
    app.exec_()

