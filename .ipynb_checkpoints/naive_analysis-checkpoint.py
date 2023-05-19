from naive_matrix import NaiveMatrix
from PageRank import page_rank

import matplotlib.pyplot as plt


x = []
y1 = []

for i in range(10, 101, 10):
    x.append(i)
    count = page_rank("all_wiki", "links.tsv", i)
    y1.append(count)
    print(i, count)
    
# Scatter plots
plt.scatter(x, y1)

# Axis labels
plt.xlabel('Size of Matrix')
plt.ylabel('Number of Multiplications')

# Title
plt.title('Time Complexity of Naive Matrix')

# Display the plot
plt.show()