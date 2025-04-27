# Pickle Example
import pickle

data = {"key": "value"}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
