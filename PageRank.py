import numpy as np
import os




def page_rank(folder, links):
    num_articles = 100

    terms_to_article_names = {}

    all_art_names = os.listdir(folder)[:num_articles]

    # all_art_names = os.listdir(folder)


    for test_file in all_art_names:

        content = open(f"{folder}/" + test_file).read().replace("\n", " ").lower().split(" ")

        for term in set(content):

            if term in terms_to_article_names:

                terms_to_article_names[term].add(test_file)

            else:

                terms_to_article_names[term] = {test_file}
            #terms_to_article_names[term] = list(set(terms_to_article_names[term]))

    all_links = np.genfromtxt(
        links,
        dtype="str",
        delimiter="\t",
        skip_header = 11
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


