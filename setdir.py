import pickle

with open("sounds.pickle", "rb") as f:
    sound_dir = pickle.load(f)
    if str(type(sound_dir)) == "<class 'str'>":
        print("it was string so making it dir")
        sound_dir = {}
    else:
        print("was not string??")

try:
    while True:
        print("When done press ctrl + C")
        sound_dir[input("NAME of new sound\n>>>")] = input("full PATH to new sound\n>>>")

except KeyboardInterrupt:
    print("Now we are done.")

with open("sounds.pickle", "wb") as f:
    pickle.dump(sound_dir, f)

print("Done now!")
