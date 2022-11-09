import tkinter
from playsound import playsound
import pickle

try:
    with open("sounds.pickle", 'rb') as pickle_file:
        sound_dir = pickle.load(pickle_file)

except:
    with open("sounds.pickle", 'wb') as pickle_file:
        pickle.dump("", pickle_file)
        print("New picklefile was created. Restart program.")
        exit()

gui = tkinter.Tk()
gui.geometry("300x300")

def pSound(path):
    playsound(path)

print(type(sound_dir))

class myButton:
    def __init__(self, label, sound_path):
        self.label = label
        self. sound_path = sound_path

    def reg(self):
        b1 = tkinter.Button(gui, text =self.label, command=  lambda: pSound(self.sound_path))
        b1.pack()


for name, path in sound_dir.items():
    myButton(name, path).reg()


gui.mainloop()