# Created a Codon:Aminoacid dictionary in a separate module called Cod_Tab
import Cod_Tab
from Bio import SeqIO
# Import records from fasta file and put them in a list
seq_record=SeqIO.parse("SPLC_FASTA_file.txt", "fasta")
seq_list=[]
for i in seq_record:
    seq_list.append(i.seq)
# Assuming the first record includes the DNA coding strand s.
s=seq_list[0]
if len(s)>1000:
    raise Exception('max length of the string should be 1000')
# Definition of the function that transcribes the DNA coding strand in pre-mRNA
def dna_rna(s):
    u=''
    for i in s:
        if i=='T':
            u=u+'U'
        else:
            u=u+i
    return u
# Definition of the function that returns the location of the sub-string t within the string s.
# The assumption of the exercise is that only one solution will exist, therefore this function will return a single couple of
# start-end numbers in a list format.
def sub_str_location(s,t):
    # Iteration on the string s
    for i in range(len(s)):
        if len(s)-i >= len(t): # Verification if the remaining of the string is still longer than t
            if t[0]==s[i]:
                stop=0
                n=1
                while (n in range(1,len(t))) and stop!=1:
                    if t[n]==s[i+n]:
                        n+=1
                        if n==len(t):
                            loc_start=i     # This is the position of the first element of the intron
                            loc_end=i+len(t) # This is the position of the first element right after the intron end
                    else:
                        stop=1
    return [loc_start,loc_end]
# The other assumption is that the introns will not overlap each other
# Creation of the list with rna strings (the pre-mRNA will be in the position rna[0])
rna=[]
for i in seq_list:
    rna.append(dna_rna(i))
# Creation of the list with all starts and ends of introns
locations_list=[]
for i in range(1,len(rna)):
    locations_list.append(sub_str_location(rna[0],rna[i]))
# Merging all starts and ends in a single list (including the extremes of pre-mRNA)
merge_list=[0,len(rna[0])]
for i in range(len(locations_list)):
    merge_list.append(locations_list[i][0])
    merge_list.append(locations_list[i][1])
# Since the assumption is that the introns will not overlap, a sorted list of merge_list numbers will provide the points where
# to slice the pre-mRNA.
merge_list.sort()
m_rna=''
index=0
while index<len(merge_list):
    m_rna+=rna[0][merge_list[index]:merge_list[index+1]]
    index+=2
# Translate the m-RNA into protein
# Convert the string m_rna in a list of codons
codon_list=[]
first=m_rna[0::3]
second=m_rna[1::3]
third=m_rna[2::3]
tot_cod=len(first)
for i in range(tot_cod):
    codon_list.append(first[i]+second[i]+third[i])
# Mapping the codons to aminoacids and print the resulting protein
protein=''
for cod in codon_list:
    protein+=Cod_Tab.RNA_dictionary[cod]
protein=protein[:-1]

print(protein)
