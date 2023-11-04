import numpy as np
import math
from client import Player
import pickle

p = Player(1, 2, 3, 4, (255, 200, 100))

data = pickle.dumps(p)

read = pickle.loads(data)