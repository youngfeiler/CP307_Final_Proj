import numpy as np
import os
from sparse_matrix import SparseMatrix


def page_rank(folder, links, n):

    def get_top_rows_by_nonzero_count(array, n):
        row_indices = np.arange(len(array))

        nonzero_counts = np.count_nonzero(array, axis=1)

        sorted_indices = np.argsort(nonzero_counts)[::-1] # Sort indices in descending order

        top_indices = sorted_indices[:n]  # Select the top n indices

        return array[row_indices[top_indices], :]

    num_articles = 100

    terms_to_article_names = {}

    # all_art_names = os.listdir(folder)[:num_articles]
    all_art_names = os.listdir(folder)

    # all_art_names = os.listdir(folder)

    # Get the length of the actual list of articles

    for test_file in all_art_names:

        content = open(f"{folder}/" + test_file).read().replace("\n", " ").lower().split(" ")

        for term in set(content):

            if term in terms_to_article_names:

                terms_to_article_names[term].add(test_file)

            else:

                terms_to_article_names[term] = {test_file}
            # terms_to_article_names[term] = list(set(terms_to_article_names[term]))

    all_links = np.genfromtxt(
        links,
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

    M = get_top_rows_by_nonzero_count(M, n)
    M = SparseMatrix(M)
    # Get the amount of articles (amount of rows and columns in our matrix)
    length = 4604

    # Make a random array which is that length
    v = np.random.random(length)

    counter = 1

    tolerance = 0.01

    while True:
        new_v = np.dot(v, M)

        dif = np.abs(new_v - v)

        max_dif = np.mean(dif)

        if max_dif < tolerance:
            break

        v = new_v.copy()

        counter += 1
    i = 0

    total = 0
    counter = 6
    M2 = M.copy
    while i < counter:
        M2,count = M2*M
        total += count


    print(f"Convergence achieved after {counter} iterations.")

    return total
