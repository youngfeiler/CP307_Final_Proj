from naive_matrix import NaiveMatrix
from sparse_matrix import SparseMatrix


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

    #print(mat1.to_naive())


    res_mat,count_naive = mat3*mat4
    rslt= NaiveMatrix(res_mat)
    print(rslt)
	
    
    res_mat2,count_sparse = mat1*mat2
    rslt= SparseMatrix(res_mat2)
    print(rslt.to_naive())

    print(count_naive,count_sparse)

