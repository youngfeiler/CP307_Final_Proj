from naive_matrix import NaiveMatrix
from sparse_matrix import SparseMatrix

from PageRank import page_rank
import matplotlib.pyplot as plt


if __name__ == '__main__':
    arr1 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    arr2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    mat1 = SparseMatrix(arr1)
    mat2 = SparseMatrix(arr2)

    #mat3 = NaiveMatrix(arr1)
    #mat4 = NaiveMatrix(arr2)

    #res_mat,count_naive = mat3*mat4

    #rslt= NaiveMatrix(res_mat)

    #print(rslt)
    res_mat2, count_sparse = mat1 * mat2




    for i in range(10):
        print(mat2.sparse)
        res_mat2,count_sparse = res_mat2*mat2

        print(res_mat2.to_string())

    #print(count_naive,count_sparse)

    M = page_rank("all_wiki", "links.tsv")

    sparse_m = SparseMatrix(M)

    total = 0
    y = []
    x = [1,2,3,4,5,6,7,8,9]

    print(len(M))

    import matplotlib.pyplot as plt
    def EXAMPLE_PLOT_INFO():
        # Sample data
        x = [1, 2, 3, 4, 5]
        y1 = [2, 4, 6, 8, 10]
        y2 = [1, 3, 5, 7, 9]
        labels = ['Data 1', 'Data 2']

        # Scatter plots
        plt.scatter(x, y1, label=labels[0])
        plt.scatter(x, y2, label=labels[1])

        # Axis labels
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Title
        plt.title('Scatter Plot')

        # Legend
        plt.legend(title='Legend')
    
        # Display the plot
        plt.show()

    for i in range(9):
        print(f'Starting step: {i}, len: {len(sparse_m.sparse)}')
        sparse_m, count = sparse_m*sparse_m
        total += count
        y.append(total)
        print(f'Finished step: {i}')
    print(y)


    plt.scatter(x,y)
    plt.show()


