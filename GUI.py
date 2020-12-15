import PySimpleGUI as sg
from sys import argv, exit
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
from b64_images import *

sg.theme('DarkBlue16')  # theme

win = [  # creating the window layout
      [sg.Text("Press the button to start!", font="dubai 18", justification="center")],

      [sg.Button("", image_data=continue_b64, pad=(0, 15), border_width=0, key="start",
               button_color=(sg.theme_background_color(), sg.theme_background_color()),)],

      [sg.Multiline(default_text='Your transformed text will be here', enable_events=True, key="multiline",
                  size=(50, 3), border_width=0, font="dubai 13")],

      [sg.Text("Status", font="dubai 18", key="status", size=(25, 2), justification="c", enable_events=True)]]

trWin = sg.Window("Image to text", win,
                  keep_on_top=True,
                  size=(450, 315),  # creating the window
                  alpha_channel=0.9,
                  element_justification="c")


class MyWidget(QtWidgets.QWidget):  # snipping tool
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
    window.show()  # function to start the snipping tool
    app.exec_()
