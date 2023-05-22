# CP307_Final_Proj
CP307 DSA Final Project Repo

all_wiki - dataset of Wikipedia articles
analysis.ipynb - the notebook we used to run our tests and produce our graphs
links.tsv - dataset of links in between Wikipedia articles 
naive_matrix.py - our naive matrix implementation
PageRank.py - our page rank implementation
scipyMatrix.py - our scipy matrix implementation
sparse_matrix.py - our sparse matrix implementation 

Our goal was to see if we could build our own sparse matrix multiplication method that would perform better than a naive one to show the benefits of sparse matrices on a page rank implementation. This was succesful, although the built in matrix multiplication methods performed significantly better than ours, their big O was the same as ours. 

To run our experiment, run the analysis.ipynb file. 