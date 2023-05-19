from naive_matrix import NaiveMatrix
from sparse_matrix import SparseMatrix

from PageRank import PageRank
import matplotlib.pyplot as plt

import time

def test():

    start = time.time()

    pagerank = PageRank("all_wiki", "links.tsv", 300)

    pagerank.make_initial_matrix()

    end_1 = time.time()

    print(f'Time to initialize: {end_1-start}')

    # pagerank.find_convergence()
    end_2 = time.time()
    # print(f'Time to find convergence: {end_2-end_1}')

    M, total = pagerank.do_multiplication_6_times(SparseMatrix)
    end_3 = time.time()
    print(f'Time to multiply 6 times: {end_3 - end_2} and count: {total}')

    print(pagerank.M)




if __name__ == '__main__':

    test()


    # arr1 = [
    #     [1, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 1]
    # ]
    #
    # arr2 = [
    #     [1, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 1]
    # ]
    #
    # mat1 = SparseMatrix(arr1)
    # mat2 = SparseMatrix(arr2)
    #
    # res_mat2, count_sparse = mat1 * mat2
    #
    # for i in range(10):
    #     print(mat2.sparse)
    #     res_mat2,count_sparse = res_mat2*mat2
    #
    #     print(res_mat2.to_string())
    #
    #
    # sparse_m = SparseMatrix(M)
    #
    # total = 0
    # y = []
    # x = [1,2,3,4,5,6,7,8,9]
    #
    # print(len(M))
    #
    # import matplotlib.pyplot as plt
    # def EXAMPLE_PLOT_INFO():
    #     # Sample data
    #     x = [1, 2, 3, 4, 5]
    #     y1 = [2, 4, 6, 8, 10]
    #     y2 = [1, 3, 5, 7, 9]
    #     labels = ['Data 1', 'Data 2']
    #
    #     # Scatter plots
    #     plt.scatter(x, y1, label=labels[0])
    #     plt.scatter(x, y2, label=labels[1])
    #
    #     # Axis labels
    #     plt.xlabel('X-axis')
    #     plt.ylabel('Y-axis')
    #
    #     # Title
    #     plt.title('Scatter Plot')
    #
    #     # Legend
    #     plt.legend(title='Legend')
    #
    #     # Display the plot
    #     plt.show()
    #
    # for i in range(9):
    #     print(f'Starting step: {i}, len: {len(sparse_m.sparse)}')
    #     sparse_m, count = sparse_m*sparse_m
    #     total += count
    #     y.append(total)
    #     print(f'Finished step: {i}')
    # print(y)
    #
    #
    # plt.scatter(x,y)
    # plt.show()


