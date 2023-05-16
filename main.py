from naive_matrix import naive_matrix

if __name__ == '__main__':
    matrix1 = [
        [1, 3, 5],
        [2, 4, 6]
    ]

    matrix2 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    mat1 = naive_matrix(matrix1)
    mat2 = naive_matrix(matrix2)

    print(mat1 * mat2)

