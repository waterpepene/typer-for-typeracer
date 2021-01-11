from functions import *
from GUI import *

pt.pytesseract.tesseract_cmd = r'G:\Tesseract\tesseract.exe'       # path to tesseract executable

while True:
    event, values = trWin.read()

    if event in (None, 'Exit'):
        exit()

    if event in (None, "start"):
        t.Thread(target=start, daemon=True).start()