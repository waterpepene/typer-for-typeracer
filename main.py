import pytesseract as pt
from functions import *
import PySimpleGUI as sg
from GUI import *
from sys import exit
from os import remove

pt.pytesseract.tesseract_cmd = r'E:\Tesseract\tesseract.exe'        # path to tesseract executable


while True:
    event, values = trWin.read()

    if event in (None, "kot"):
        if kot1or0 == 1:
            kot1or0 = 0
            trWin.TKroot.wm_attributes("-topmost", kot1or0)
        elif kot1or0 == 0:
            kot1or0 = 1
            trWin.TKroot.wm_attributes("-topmost", kot1or0)

    if event in (None, 'Exit'):  # if user closes window
        exit()

    if event in (None, "start"):
        trWin["status"].update("Started")
        trWin.Refresh()

        trWin["status"].update("Take snip.")
        trWin.Refresh()

        takeSnip()
        trWin["status"].update("Converting to text...")
        trWin.Refresh()
        text = pt.pytesseract.image_to_string("image.png")
        print(text)

        trWin["status"].update("Correcting...")
        trWin.Refresh()

        try:
            cortext = correct(text)
            print(cortext + "text")
            trWin["status"].update("Done! Press shift to write it!")
            trWin.Refresh()

            write(cortext)

            trWin["status"].update("Status")
            trWin.Refresh()
            remove("image.png")

        except IndexError:
            trWin["status"].update("No text recognized!")
            trWin.Refresh()
            time.sleep(4)
            trWin["status"].update("Status")
            trWin.Refresh()
            remove("image.png")