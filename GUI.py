import PySimpleGUI as sg
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab

                                                        # variables and b64 images
b64_img = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxEAAAsRAX9kX5EAAAKASURBVDhPhZTLb4xhFMZ/rapq45KGSBGJRSXWIrFgoaQLJBbd2Ikdf4CNhQ2i2NgRiQWxUITGNS61cG8piWtsUFJFQoVqjRr1O998085MpzzJ037v7TnnvOd5h0Lch2UPoOMu1KdTE+Im1Lr3vGea06kElel/bsPSCrjkZ1MVXOn4h6ib6mrgnJ9rPXPmDqzKraSCW6FmMpzwc2aM3bRk+gSiITYLzrqnKZ2q9ezxA+nZRHCfgkeh9Rf8jHGgnGgZMX7D8EnYsyWnVTEp/sgZXR58C9nlsNiSYz4W5k6B1RvglKycXSI2rN5eSz4M9xy+lwPJQRGi1a8UegODK6CxVLQWWkyhSKzVprTDLYfPZK/M5AXNnB8y89osy4nKhfEdCLHdip2FGw5tNC/lNzmSFxyRXiEDsqxoHiVi3hQv5Ff5R47ZRsRERIloXY/kJ/gSC4Xod89D0ILjxQJF0UWS6Ro37Iddc2BRbnoMdTB1Hcwzk0MG/eDUqFggmlGEi6k1ShqQzXpQM2u5HIzcbTnNOrqoisKSE5+FNUq7uROubYPLmjTuOYGZlDX/aIblTJs24IINeOxwZKUe3QHrzbQ6t2N8pskdnvalNNi5MmLRTX8Hkib02PmhiXzaAm3HdEhS8iao0uZhzAQl1uiUNhZ7QOd1jbwd2gvL1w29m9NqI0pFxnto09iNsGA+NMQLKPGZbkne+TifdsOTjXDQevtiPW+buJP6q5ak7XtUKuezceZ3b98RX4oO8NXyTg7mBePpRQaZj7lIT2UYvMi0olB0yFL7nQix5/KzzI52WYTHdAI2ke8yDhWZtgBx93qcaTICxAsbvdNCRIDCIP9DyX74Czey8LJe6Ov6AAAAAElFTkSuQmCC'
b64_pin = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxMAAAsTAQCanBgAAALVSURBVDhPrZTPTxNREMdnF2h3+wOB0BJFTYxEJZgeiOGHxIMJJBw8mHjSg4l6MFEOHAxRryoejBcOEk4e1YNHE/kHJEFIgFhDIZFgbQgFSne3u9vd7nvPecujoFRqop9ksjPT2W/nvXlvJRDQoaF6aWPjPqyuXmO6fobZtkss69O6aT45USh8FmVV8QXZyEg3LC29h1SqFUwTE8z/kT8Lpul8MYzLvZ43tZM8HJk9f34alpcnYX6+FQqFPTGOJEFYVYMRWX4oMlWRYW3tKSSTR8DzROpXJBRlktQqwqrIkMkMQLEowoOU8I80QmZFWBUZdN0V/gEYpfDdMLwNQl6KVFUk2tPzTMpmH0OpJFI7EOwsrWlQtG0IMfZO6eh4EIvHu0DTzjPTVD3LSm/Z9sdjm5vfxCs+UqG9vTZgGKPgukMYqyVCQHddmrNtOYiiKiZltJpQCKLxOCi4p4Cd8+G5WJcxzfGvrjt8xXH8IZTP4XQoFFIIOWdRyrYJWWmn9E0AYJAXcEFu3A9EoxBtaEBvB8t1IZnPv+hynBEelwV/Z72//yTMzKxI+by8K8qf3NRYDIKKgh5vlEFqe9uesu3m25RavK4i8c7Oew2xmMyPzX4x3+fLFnAvWFOjBhk7zuOKgmR0FCCdvhnA5Sj19WUh38JhCASDvKyMSQjBK7HO/YqCTNPCkMsd5RsfQUGlqQlqIxEINDdDBP39ODi4rOtO3mVM43FFwZKuWzjCnAhBxa7CjY2gqHzme1Cc9rKu21nP8wfCqSiojo8zVixOQF2dyByE36BFvGGZvr5H1xlLirS/PRWxE4lArWG8ll33xu4Q+ET5Od1CodVIJMXGxs7WtbVxsQtdiYR/f/8oyHnb0gK9jnMR13a1ROmpIqUlw/MWtwj5kGJs9tLc3C0se4U2gYLD/kv/yvTCQjfaD7RBHh/a4d+CYvzzxju9818EOSiKVwcGfgIZz0q94tsQ2gAAAABJRU5ErkJggg=='
kot1or0 = 1
sg.theme('DarkBlue16')  # theme

instructions = sg.PopupOK("Instructions\n This app is pretty simple to use!\nWhen you click the start button, you'll "
                          "be prompted to take a snip of the text you want converted.\nWhen the conversion is done, "
                          "you'll have to press shift to have the text written.",
                          no_titlebar=True,                                         # instructions popup
                          font="rockwell 16",
                          line_width=16,
                          keep_on_top=True)

titlebar = [[sg.Button('', image_data=b64_pin,                  # keep program in front of all programs button
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       border_width=0, key='kot', tooltip="Keeps the program in front of all other programs."),

            sg.Button('', image_data=b64_img,                   # exit button
                      button_color=(sg.theme_background_color(), sg.theme_background_color()),
                      border_width=0, key='Exit', tooltip="Exit the program")]]


win = [[sg.Column(titlebar, justification="r")],                # creating the window layout
       [sg.Text("Press the button to start!", font="rockwell 20", justification="center")],
       [sg.Button("Start!", font="rockwell 20", border_width=0, tooltip="Start", size=(7,1), pad=(0,50), key="start")],
       [sg.Text("Status", font="rockwell 20", key="status", size=(25,1), justification="c", enable_events=True)]]


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
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
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
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()                               # function to start the snipping tool
    app.exec_()

