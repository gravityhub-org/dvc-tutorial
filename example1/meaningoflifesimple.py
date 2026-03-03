import numpy as np
import nolds

def get_meaning_of_life(steps=1000):
    return 42

meaning_of_life = get_meaning_of_life()

# Save the meaning of life in a txt file
np.savetxt("meaning_of_life.txt", [meaning_of_life], fmt='%d')

# Load it out
meaning_of_life = np.loadtxt("meaning_of_life.txt", dtype=int)
print(f"Loaded the meaning of life from file: {meaning_of_life}")

