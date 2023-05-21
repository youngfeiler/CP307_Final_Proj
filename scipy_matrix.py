from scipy.sparse import csr_matrix

class scipyMatrix():

    def __init__(self, naive):
        self.naive = naive
        self.sparse = self.to_scipy()

    def to_scipy(self):
        rows = []
        cols = []
        vals = []

        if len(self.naive) > 0:

            for row in range(len(self.naive)):

                for col in range(len(self.naive[0])):

                    if self.naive[row][col] != 0:
                        rows.append(row)
                        cols.append(col)
                        vals.append((self.naive[row][col]))

        scipy = csr_matrix((vals,(rows,cols)), shape = ((len(self.naive)),(len(self.naive[0]))))

        return scipy