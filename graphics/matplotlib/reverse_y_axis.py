# https://www.tutorialspoint.com/matplotlib/matplotlib_reverse_axes.htm

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot with default axis orientation
plt.plot(x, y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Default Y-axis')
plt.show()

# Reversing the x-axis
# Reversing the y-axis
plt.plot(x, y, marker='o')
plt.gca().invert_yaxis()  # Reverse y-axis
plt.xlabel('X-axis')
plt.ylabel('Reversed Y-axis')
plt.title('Reversed Y-axis')
plt.show()
