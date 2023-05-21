import numpy as np
import os

from scipy_matrix import scipyMatrix
from scipy.sparse import csr_matrix
from sparse_matrix import SparseMatrix


class PageRank():
    def __init__(self, folder, links, n):
        self.folder = folder

        self.links = links

        self.n = n

        self.M = self.make_initial_matrix()

        self.convergence_iterations = 6

    def make_initial_matrix(self):

        terms_to_article_names = {}

        all_art_names = os.listdir(self.folder)[:self.n]

        # Get the length of the actual list of articles

        for test_file in all_art_names:

            content = open(f"{self.folder}/" + test_file).read().replace("\n", " ").lower().split(" ")

            for term in set(content):

                if term in terms_to_article_names:

                    terms_to_article_names[term].add(test_file)

                else:

                    terms_to_article_names[term] = {test_file}
                # terms_to_article_names[term] = list(set(terms_to_article_names[term]))

        all_links = np.genfromtxt(
            self.links,
            dtype="str",
            delimiter="\t",
            skip_header=11
        )

        M = np.eye(len(all_art_names))

        for pair in all_links:
            first_page, second_page = pair
            if first_page + ".txt" in all_art_names and second_page + ".txt" in all_art_names:
                index_1 = all_art_names.index(first_page + ".txt")
                index_2 = all_art_names.index(second_page + ".txt")

                M[index_1, index_2] += 1

        for i in range(M.shape[0]):
            M[i] /= M[i].sum()

        return M

    def get_top_rows_by_nonzero_count(self, n):

        array = self.M

        row_indices = np.arange(len(array))

        nonzero_counts = np.count_nonzero(array, axis=1)

        sorted_indices = np.argsort(nonzero_counts)[::-1]  # Sort indices in descending order

        top_indices = sorted_indices[:n]  # Select the top n indices

        return array[row_indices[top_indices], :]

    def do_multiplication_6_times(self, matrixClass):

        if matrixClass == scipyMatrix:

            M = matrixClass(self.M).sparse

            M2 = matrixClass(self.M).sparse

            i = 0

            # counter = self.convergence_iterations
            counter = 6
            while i < counter:
                M2 = M2.multiply(M)

                i += 1

            return M

        else:

            M = matrixClass(self.M)

            M2 = matrixClass(self.M)

            i = 0

            total = 0

            #counter = self.convergence_iterations
            counter = 6
            while i < counter:

                M2, count = M2 * M

                total += count

                i += 1

            return M, total

    def find_convergence(self):
        # Get the amount of articles (amount of rows and columns in our matrix)
        length = self.n

        # Make a random array which is that length
        v = np.random.random(length)

        counter = 1

        tolerance = 0.01

        while True:
            new_v = np.dot(v, self.M)

            dif = np.abs(new_v - v)

            max_dif = np.mean(dif)

            if max_dif < tolerance:
                break

        v = new_v.copy()

        counter += 1

        return counter