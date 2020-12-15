import keyboard as kb
from time import sleep
from GUI import *
from os import remove
import pytesseract as pt
import threading as t

interval = 0.02  # time waited between the input of letters


def write(text):
    trWin["status"].update("Done! Press shift to write it!\n"
                           "Right CTRL to cancel.")
    trWin.Refresh()

    while "waiting":
        if kb.is_pressed("shift"):
            [kb.write(word, delay=interval) for word in text]
            trWin["status"].update("Status")
            trWin["multiline"].update("Your transformed text will be here")
            trWin.Refresh()
            break

        elif kb.is_pressed("right ctrl"):
            trWin["status"].update("Status")
            trWin["multiline"].update("Your transformed text will be here")
            trWin.Refresh()
            break


def start():
    trWin.Hide()

    takeSnip()
    trWin.UnHide()

    text = pt.pytesseract.image_to_string("image.png")
    trWin["multiline"].update(text)
    print(text)

    try:
        t.Thread(target=write, args=(text,), daemon=True).start()
        print("_" * 60)

    except IndexError:
        trWin["status"].update("No text recognized!")
        trWin.Refresh()

        sleep(3)

        trWin["status"].update("Status")
        trWin.Refresh()

    remove("image.png")
