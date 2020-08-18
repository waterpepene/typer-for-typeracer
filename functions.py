import keyboard as kb
import time

letters = "qwertyuiopasdfghjklzxcvbnm"

def write(text):
    waiting = True
    while waiting:
        if kb.is_pressed("shift"):
            waiting = False                     # function to write down text given to the text parameter
            for word in text:
                kb.write(word)
                time.sleep(0.08)


def correct(giventext):
    replace = ["{", "|", "\n", "1", "’", "‘", "Nou", "Ata", "“"]
    strip = ["[", "\\", ">", "‘", "’", "(", "|"]
    text = giventext

    if replace[2] in text:
        lastix = text.index(replace[2]) - 1
        for letter in letters:                                                   # this function corrects mistakes
            if text[lastix] in letter:
                pass
            else:
                text = text.replace(replace[2] + replace[2], replace[2])
                text = text.replace(replace[2], " ")

    for char in strip:
        if char in text[0]:
            text = text.strip(char)

    if replace[0] in text:
        text = text.replace(replace[0], "T")

    if replace[1] in text:
        text = text.replace(replace[1], "I")

    if text[0] == replace[3] in text:
        text = text.replace(replace[3], "I")

    if text[0] == replace[3]:
        text = text.replace(replace[3], "I")

    elif replace[4] in text:
        text = text.replace(replace[4], "'")

    if replace[5] in text:
        text = text.replace(replace[5], "'")

    if replace[6] in text:
        text = text.replace(replace[6], "You")

    if replace[7] in text:
        text = text.replace(replace[7], "At a")

    if replace[8] in text:
        text = text.replace(replace[8], "\"")

    return text
