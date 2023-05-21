from naive_matrix import NaiveMatrix
from collections import defaultdict


class SparseMatrix(NaiveMatrix):
    def __init__(self, a):

        # Initializes to the liking of the Naive Matrix
        super().__init__(a)

        self.sparse = self.convert_to_sparse()

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

        return rsl_mat,count


    # def __mul__(self, b):
    #
    #     count = 0
    #
    #     result = SparseMatrix([])
    #
    #     # Check if the column of A is equal to the row of B
    #     for a_el in self.sparse:
    #
    #         for b_el in b.sparse:
    #
    #             if a_el[1] == b_el[0]:
    #
    #                 found = False
    #
    #                 val = a_el[2] * b_el[2]
    #                 count +=1
    #                 # Check if there is already a value in our resulting matrix
    #                 if len(result.sparse) > 0:
    #                     for el in result.sparse:
    #                         if el[0] == a_el[0] and el[1] == b_el[1]:
    #                             el[2] += val
    #                             found = True
    #
    #                 # right now we need to iterate through all of the non-zero entries of both matricies. Inside that
    #                 # for loop, we have a check that might be the issue. Replace that process with a dictionaryof dictionaries
    #                 # first dict maps rows to another dictionary, that one maps column indicies to a list
    #                 # store all the values in that list and the final step
    #
    #
    #                 if found == False:
    #
    #                 # we want to append a row of A col of B value
    #                     result.sparse.append([a_el[0], b_el[1], val])
    #
    #     return result, count

    def to_naive(self):
        rslt = [[0 for i in range(self.cols)] for i in range(self.rows)]
        for el in self.sparse:
            rslt[el[0]][el[1]] = el[2]
        return

    def to_string(self):
        return self.sparse

    def copy(self):
        return self
        #to_return = SparseMatrix(
        #for el in self.sparse:
            #to_return.append(el)
        #return to_return
