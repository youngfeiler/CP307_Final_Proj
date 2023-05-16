class naive_matrix():
    def __init__(self, a):
        self.a = a
        self.rows = len(a)
        self.cols = len(a[0])

    def make_empty_result_matrix(self, b):

        b_cols = b.cols

        return [[0 for col in range(b_cols)]for row in range(self.rows)]



    def __mul__(self, b):

        a_rows = self.rows
        a_cols = self.cols

        b_rows = b.rows
        b_cols = b.cols


        if self.cols == b.rows:
            rslt = self.make_empty_result_matrix(b)

            for i in range(0, a_rows):
                for j in range(0, b_cols):
                    for k in range(0, b_rows):
                        rslt[i][j] += self.a[i][k] * b.a[k][j]

            print("Multiplication of given two matrices is:")
            for i in range(0, a_rows):
                for j in range(0, b_cols):
                    print(rslt[i][j], end=" ")
                print("\n", end="")

        else:
            raise Exception("Matrix dimensions are not compatible for multiplication.")

