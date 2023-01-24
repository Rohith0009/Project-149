from tkinter import *
import random
root = Tk()
root.title("Random Word")
root.geometry("1600x1600")
root.configure(background="pale green")
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

RandomLabel = Label(root, text="Click On Generate Random Word", font=('Arial', 30))
RandomLabel.place(relx=0.5, rely=0.25)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate():
    global letters, RandomNum1, RandomNum2, RandomNum3, RandomNum4, RandomNum5, RandomLetter1, RandomNum3, RandomLetter2, RandomLetter3, RandomLetter4, RandomLetter5
    RandomNum1 = random.randint(0,25)
    RandomNum2 = random.randint(0,25)
    RandomNum3 = random.randint(0,25)
    RandomNum4 = random.randint(0,25)
    RandomNum5 = random.randint(0,25)
    RandomLetter1 = letters[RandomNum1]
    RandomLetter2 = letters[RandomNum2]
    RandomLetter3 = letters[RandomNum3]
    RandomLetter4 = letters[RandomNum4]
    RandomLetter5 = letters[RandomNum5]
    RandomWord = f"{RandomLetter1}{RandomLetter2}{RandomLetter3}{RandomLetter4}{RandomLetter5}"
    RandomLabel['text'] = RandomWord

RandomBTN = Button(root, text="Generate Random Word", command=generate, font=('Arial', 30))
RandomBTN.place(relx=0.5, rely=0.1)

root.mainloop()