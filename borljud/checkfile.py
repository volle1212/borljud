import pickle

with open("sounds.pickle", "rb") as f:
    print(pickle.load(f))