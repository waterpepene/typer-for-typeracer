import pytesseract as pt
from functions import *
from GUI import *
from os import remove

tesseract_path = r'E:\Tesseract\tesseract.exe'       # change this to your own path
pt.pytesseract.tesseract_cmd = tesseract_path        # path to tesseract executable


while True:
    event, values = trWin.read()

    if event in (None, 'Exit'):
        exit()

    if event in (None, "start"):
        trWin["status"].update("Started")
        trWin.Refresh()
                                                # trWin["status"] is the status label
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
            cortext = correctText(text)
            print(cortext)
            trWin["status"].update("Done! Press shift to write it!")
            trWin.Refresh()

            write(cortext)

            trWin["status"].update("Status")
            remove("image.png")
            trWin.Refresh()
            print("_"*60)

        except IndexError:
            trWin["status"].update("No text recognized!")
            trWin.Refresh()
            sleep(3)
            trWin["status"].update("Status")
            trWin.Refresh()
            remove("image.png")