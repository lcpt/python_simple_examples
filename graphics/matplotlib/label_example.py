# Example taken from https://python-graph-gallery.com/4-add-title-and-axis-label

# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# create dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
x_pos = np.arange(len(bars))
 
# Create bars and choose color
plt.bar(x_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('My title')
plt.xlabel('categories')
plt.ylabel('values')
 
# Create names on the x axis
plt.xticks(x_pos, bars)
 
# Show graph
plt.show()
