from sparse_matrix import SparseMatrix
from PageRank import page_rank

import matplotlib.pyplot as plt


x = []
y2 = []

for i in range(100, 1001, 100):
    x.append(i)
    count = page_rank("all_wiki", "links.tsv", i)
    y1.append(count)
    print(i, count)

# Scatter plots
plt.scatter(x, y2)

# Axis labels
plt.xlabel('Size of Matrix')
plt.ylabel('Number of Multiplications')

# Title
plt.title('Time Complexity of Sparse Matrix')
    
# Display the plot
plt.show()