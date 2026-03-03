import numpy as np
import pylab as plt

def get_meaning_of_life(steps=1000):
    x = 0.5  # Starting condition
    r = 3.9  # The 'chaos' parameter (anything above 3.57 is chaotic)
    system_output = []
    
    for _ in range(steps):
        x = r * x * (1 - x) # The deterministic formula
        system_output.append(x)
    return np.array(system_output)

# Use 'nolds' to measure the chaos (The Lyapunov Exponent)
data = get_meaning_of_life()
chaos_level = nolds.lyap_r(data)

# The Reveal
print(f"Analyzing the deterministic chaos of existence...")
print(f"Chaos Level: {chaos_level:.4f}")
print(f"The meaning of life is approximately: {int(chaos_level * 10000)}")

# Save the meaning of life in a txt file
np.savetxt("meaning_of_life.txt", [int(chaos_level * 10000)], fmt='%d')

# Load it out
meaning_of_life = np.loadtxt("meaning_of_life.txt", dtype=int)
print(f"Loaded the meaning of life from file: {meaning_of_life}")

