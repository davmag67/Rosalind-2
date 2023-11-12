import numpy as np
# Inputs
n=10
adj_list=np.array([[1,2],[2,8],[4,10],[5,9],[6,10],[7,9]])
if n>1000:
    raise Exception('The number of nodes cannot exceed 1000')
# A property of a tree states the following: any tree with n nodes has exaclty n-1 edges.
# Therefore it will be sufficient to compare the number of rows of the array with n-1
n_rows=adj_list.shape[0]

if n_rows>=n:
    raise Exception('The given adjacency list is describing a graph with cycles')
else:
    min_edges=(n-1)-n_rows
print(min_edges)