import keyboard as kb
from time import sleep

interval = 0.04    # time waited between the input of letters


def write(text):
    waiting = True
    while waiting:
        if kb.is_pressed("shift"):
            waiting = False                     # function to write down text given to the text parameter
            for word in text:
                kb.write(word)
                sleep(interval)


def correctText(given_text):           # this function corrects mistakes from the image to text conversion
    replace = {"{": "T", "|": "I", "’": "'", "‘": "'", "Nou": "You", "Ata": "At a", "“": "\""}
    strip = ["[", "\\", ">", "‘", "’", "(", "|"]
    letters = "qwertyuiopasdfghjklzxcvbnm"

    if "\n" in given_text:
        lastix = given_text.index("\n") - 1
        for letter in letters:
            if given_text[lastix] in letter:
                pass
            else:
                given_text = given_text.replace("\n" + "\n", "\n").replace("\n", " ")

    for char in strip:
        if char in given_text[0]:
            given_text = given_text.strip(char)

    for symbol in replace:
        if symbol in given_text:
            given_text = given_text.replace(symbol, replace[symbol])

    return given_text
