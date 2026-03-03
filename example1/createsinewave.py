import numpy as np
import pylab as plt
import scienceplots
plt.style.use(['science', 'ieee', 'bright'])

# Load the meaning of life:
meaning_of_life = np.loadtxt("meaning_of_life_copy.txt")

# Create a sine wave:
x = np.linspace(0, 10, 100)
y = meaning_of_life * np.sin(x)

# Plot the meaning of life as a sine wave:
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Meaning of Life Sine Wave', color='blue')
plt.title('The Meaning of Life as a Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Meaning of Life * sin(X)')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.legend()
plt.grid()
plt.savefig("meaning_of_life_sine_wave.pdf")
plt.close()
