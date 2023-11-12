'''
The number of internal nodes of an unrooted binary tree is equal to the number of leaves minus 2.
There are a couple of ways to demonstrate it:
1) In a recursive way. Starting from a number n=3 of leaves.
    For n=3 we have a star wiht 1 internal node and 3 leaves
    To go from 3 to 4 leaves we cannot add en edge to the internal node already present 
    (otherwise will have degree 4, not allowed).
    we must add to one of the current leaves. If we add 2 new leaves to a former leave, 
    this one will become an internal node (with degree 3), therefore the net increase of leaves will be +1.
    A similar situation will happen if we want to add one more leave. We must add to one of the current leaves,
    giving a net increase of one leave. Everytime we add 1 leave we also have an increase of internal node of 1.
    Therefore, starting with the initial condition of 3 leaves and 1 internal node, this difference of 2 will
    continue to be preserved.
2) Using one theorem (already applied with the Rosalind exercise TREE) that any tree with N nodes will have N-1 Edges,
    plus two more observations related to the trees, we can state the following:
        Let's call:
            E = total number of edges of the tree
            L = number of leaves
            IN = number of internal nodes
            N = total number of nodes
        we can write 3 equations:
            1) 2E = L + 3*IN (the number of leaves edges + 3 times the number of internal nodes (because each has 3 edges) 
                              will give twice the number of total edges, because with the sum we are counting twice the edges )
            2) N = L + IN (the total number of nodes is equal to the leaves plus the internal nodes)
            3) E = N-1 (this is the theorem stating that the number of edges in a tree is equal to the number of nodes minus 1)
    Resolving this system for IN we will find this relationship: IN = L - 2
 '''
# Assigning the value to n as number of leaves
n=4
if n<3 or n>10000:
    raise Exception('n is out of the allowed range of 3 to 10000')
# Calculate the number of internal nodes
output=n-2
print(output)
