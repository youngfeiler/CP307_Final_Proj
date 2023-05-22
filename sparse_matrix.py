from naive_matrix import NaiveMatrix
from collections import defaultdict


class SparseMatrix(NaiveMatrix):
    def __init__(self, a):

        # Initializes to the liking of the Naive Matrix
        super().__init__(a)

        self.sparse = self.convert_to_sparse()

    def __mul__(self, sparseB):
        count = 0
        values = defaultdict(self.nesteddefaultdict)

        for a_item in self.sparse:
            for b_item in sparseB.sparse:
                ai, aj, aval = a_item
                bj, bk, bval = b_item

                if aj == bj:
                    values[ai][bk].append(aval * bval)
                    count+=1

        rsl_mat = SparseMatrix([])
        for i in range(len(self.sparse)):
            for j in range(len(sparseB.sparse)):
                if len(values[i][j]) > 0:
                    rsl_mat.sparse.append((i, j, sum(values[i][j])))

        return rsl_mat, count

    def convert_to_sparse(self):
        sparse = []
        if len(self.a)>0:

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

    def nesteddefaultdict(self):
        return defaultdict(list)

    def to_naive(self):
        rslt = [[0 for i in range(self.cols)] for i in range(self.rows)]
        for el in self.sparse:
            rslt[el[0]][el[1]] = el[2]
        return

    def to_string(self):
        return self.sparse

    def copy(self):
        return self