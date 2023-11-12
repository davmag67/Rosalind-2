import numpy as np
from Bio import SeqIO
from itertools import combinations
seq_record=SeqIO.parse("GRPH_FASTA_File.txt", "fasta")
seq_record_1=SeqIO.parse("GRPH_FASTA_File.txt", "fasta")
k=3
# Definition of a function that provide suffix and prefix of a string for a given k
def pref_suff(s,k):
    pref=''
    suff=''
    for i in range(k):
        pref=pref+s[i]
        suff=suff+s[len(s)-k+i]
    return [pref,suff]
# Creation of a dictionary with node id and the associated string
dict_all={}
for i in seq_record_1:
    dict_all[i.id]=i.seq
# Check the max lenght of the strings
str_len_list=[]
for i in dict_all:
    str_len_list.append(len(dict_all[i]))
if max(str_len_list)>10000:
    raise Exception(('string cannot be longer than 10000'))
# Creation of a dictionary with node id associated with the prefix and suffix (assuming that the node id is unique)
str_dict={}
for i in seq_record:
    str_dict[i.id]=pref_suff(i.seq, k)
# Creating the empty list that will contain the adjacency list
adj_list=[]
# Create a list with all possible nodes combinations
nodes_comb=list(combinations(str_dict,2))
# Checking the prefix ans suffix of all nodes combinations and populate the adjacency list
# There is also a first check to control that the strings are different
for i in nodes_comb:
    if dict_all[i[0]]!=dict_all[i[1]]:
        if str_dict[i[0]][1]==str_dict[i[1]][0]:
            adj_list.append([i[0],i[1]])
        elif str_dict[i[0]][0]==str_dict[i[1]][1]:
            adj_list.append([i[1],i[0]])   
# Printing in array format
a=np.array(adj_list)
print(a)

