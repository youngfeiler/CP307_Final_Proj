from naive_matrix import NaiveMatrix
from sparse_matrix import SparseMatrix

from PageRank import page_rank
import matplotlib.pyplot as plt


if __name__ == '__main__':
    arr1 = [
        [1, 0, 3],
        [0, 6, 0],
        [0, 0, 0]
    ]

    arr2 = [
        [0, 4, 0],
        [0, 9, 8],
        [1, 0, 0]
    ]

    mat1 = SparseMatrix(arr1)
    mat2 = SparseMatrix(arr2)

    mat3 = NaiveMatrix(arr1)
    mat4 = NaiveMatrix(arr2)

    res_mat,count_naive = mat3*mat4

    rslt= NaiveMatrix(res_mat)

    print(rslt)

    res_mat2,count_sparse = mat1*mat2

    rslt= SparseMatrix(res_mat2)

    print(rslt.to_naive())

    print(count_naive,count_sparse)

    M = page_rank("all_wiki", "links.tsv")

    sparse_m = SparseMatrix(M)

    total = 0
    y = []
    x = [1,2,3,4,5,6,7,8,9, 10]

    for i in range(10):
        print(f'Starting step: {i}')
        sparse_m, count = sparse_m*sparse_m
        sparse_m = SparseMatrix(sparse_m)
        total += count
        y.append(total)
        print(f'Finished step: {i}')


    plt.scatter(x,y)
    plt.show()

