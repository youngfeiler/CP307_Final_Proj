from naive_matrix import NaiveMatrix
from sparse_matrix import SparseMatrix


if __name__ == '__main__':
    arr1 = [
        [1, 2, 3],
        [5, 6, 7],
        [8, 9, 10]
    ]

    arr2 = [
        [10, 4, 1],
        [4, 9, 8],
        [1, 1, 7]
    ]

    mat1 = SparseMatrix(arr1)
    mat2 = SparseMatrix(arr2)

    mat3 = NaiveMatrix(arr1)
    mat4 = NaiveMatrix(arr2)

    #print(mat1.to_naive())
    rslt = SparseMatrix(mat1*mat2)
    print(rslt.to_naive())


