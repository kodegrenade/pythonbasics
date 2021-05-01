import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-space numbers over the range
x = np.linspace(0, 20, 200)

# Plot the sine of each x point
plt.plot(x, np.sin(x))

# Display the output
plt.show()