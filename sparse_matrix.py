from naive_matrix import NaiveMatrix


class SparseMatrix(NaiveMatrix):
    def __init__(self, a):

        # Initializes to the liking of the Naive Matrix
        super().__init__(a)

        self.sparse = self.convert_to_sparse()

    def convert_to_sparse(self):

        sparse = []

        for row in range(self.rows):

            for col in range(self.cols):

                if self.a[row][col] != 0:
                    sparse.append([row, col, self.a[row][col]])

        return sparse

    def transpose(self):
        trans = []
        for el in self.sparse:
            trans.append([el[1], el[0], el[2]])

        return trans

    def __mul__(self, b):

        count = 0
        result = []
    
        # Check if the column of A is equal to the row of B
        for a_row in self.sparse:

            for b_row in b.sparse:
                if a_row[1] == b_row[0]:
                    found = False

                    val = a_row[2] * b_row[2]
                    count +=1
                    # Check if there is already a value in our resulting matrix
                    if len(result) > 0:
                        for row in result:
                            if row[0] == a_row[0] and row[1] == b_row[1]:
                                row[2] += val
                                found = True
                    if found == False:

                    # we want to append a row of A col of B value
                        result.append([a_row[0], b_row[1], val])

        return result,count

    def to_naive(self):
        rslt = [[0 for i in range(self.cols)] for i in range(self.rows)]
        for el in self.sparse:
            rslt[el[0]][el[1]] = el[2]
        return rslt
