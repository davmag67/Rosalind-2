from Bio import SeqIO
seq_record=SeqIO.parse("LONG_FASTA_File.txt", "fasta")
# Creation of a dictionary with node id and the associated string and check max number of strings
dict_in={}
for i in seq_record:
    dict_in[i.id]=i.seq
if len(dict_in)>50:
    raise Exception('max number of strings must be 50')
# Creation of list with just the strings (will be used for the comparisons)
str_list=[]
for i in dict_in:
    str_list.append(dict_in[i])
# Check the max lenght of the strings
str_len_list=[]
for i in str_list:
    str_len_list.append(len(i))
if max(str_len_list)>1000:
    raise Exception(('string cannot be longer than 1000'))
# Creating an empty string that will contain the super-string
super_str=''
#############################################################################################
# Definition of a function that provide suffix and prefix of a string for a given k
def pref_suff(s,k):
    pref=''
    suff=''
    for i in range(k):
        pref=pref+s[i]
        suff=suff+s[len(s)-k+i]
    return [pref,suff]
############################################################################################
# Definition of a function that takes 2 strings and return an orderd list of strings and a value k in case of overlap.
# In case of no overlap it will return None.
def over_lap(str1,str2):
    if super_str=='':
        k=max(len(str1)//2,len(str2)//2)
    else:
        k=min(len(str1)//2,len(str2)//2)
    stop=0
    while k<min(len(str1),len(str2)) and stop!=1:
        if pref_suff(str1, k)[1]==pref_suff(str2, k)[0]:
            return [str1,str2,k]
            stop=1
        elif pref_suff(str1, k)[0]==pref_suff(str2, k)[1]:
            return [str2,str1,k]
            stop=1
        else:
            k+=1
#########################################################################################
# Definition of a function that takes 2 strings and a value k and return a glued string.
# The suffix of str1 will be glued over the prefix of str2 with an overlap of k
def glue(str1,str2,k):
    glue1=str1
    glue2=str2[k:]
    str_glue=glue1+glue2
    return str_glue
######################################################################################
# First round of strings compare and population of super_str with first glue
i=0
while i<len(str_list):
    j=i+1
    while j<len(str_list):
        check=over_lap(str_list[i], str_list[j])
        if check==None:
            j+=1 
        else:
            rm_1=str_list[i]
            rm_2=str_list[j]
            str_list.remove(rm_1)
            str_list.remove(rm_2)
            super_str=glue(check[0],check[1],check[2])
            break
    if check!=None:
        break
    else:
        i+=1        
# Comparisons of all the rest of strings with the super_str and make additional glues
while len(str_list)!=0:
    i=0
    while i<len(str_list):
        s_check=over_lap(super_str,str_list[i])
        if s_check==None:
            i+=1
        else:
            rm_2=str_list[i]
            str_list.remove(rm_2)
            super_str=glue(s_check[0],s_check[1],s_check[2])
            break
    if s_check==None:
        break
print(super_str)



