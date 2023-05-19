import matplotlib.pyplot as plt

x = []
# Naive
y1 = []
# Our sparse
y2 = []
# Scipy sparse
y3 = []

# Labels for legend
labels = ['Naive Matrix', 'Our Sparse Matrix', 'Scipy Sparse Matrix']

# Scatter plots
plt.scatter(x, y1, label=labels[0])
plt.scatter(x, y2, label=labels[1])
plt.scatter(x, y2, label=labels[2])

# Axis labels
plt.xlabel('Size of Matrix')
plt.ylabel('Number of Multiplications')

# Title
plt.title('Comparison of Time Complexities')

# Legend
plt.legend(title='Legend')
    
# Display the plot
plt.show()