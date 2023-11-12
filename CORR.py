from Bio import SeqIO
seq_record=SeqIO.parse("CORR_FASTA_File.txt", "fasta")
# Creation of a dictionary with node id and the associated string and check max number of strings
dict_in={}
for i in seq_record:
    dict_in[i.id]=i.seq
if len(dict_in)>1000:
    raise Exception('max number of strings must be 1000')
# Creation of list with just the strings
str_list=[]
for i in dict_in:
    str_list.append(dict_in[i])
# Check the max lenght of the strings
if len(str_list[0])>50:
    raise Exception(('string cannot be longer than 50'))
################################################################################################
# Definition of the function that calculates the reverse complement of a string
def rev_c(s):
    map={'A':'T','T':'A','C':'G','G':'C' }
    s_conv=''
    for i in s:
        s_conv+=map[i]
    s_comp=s_conv[::-1]
    return s_comp
##############################################################################################
# Definition of the function that calculates the Hamming distance
def d_h(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count
#############################################################################################
# Create a class Sequence having a string along with its status as attributes: 
# NC (Not Checked), Correct, Incorrect
class Seq:
    def __init__(self,string,status):
        self.string=string
        self.status=status
# Create a list with Seq objects
seq_list_obj=[]
for i in str_list:
    seq_list_obj.append(Seq(i,'NC'))
# Checking each other all elements of the objects list and assess if they are correct or not
i=0
while i<len(seq_list_obj):
    j=i+1
    while j<len(seq_list_obj):
        if (seq_list_obj[i].string==seq_list_obj[j].string) or (seq_list_obj[i].string==rev_c(seq_list_obj[j].string)):
            seq_list_obj[i].status='correct'
            seq_list_obj[j].status='correct'
        j+=1
    i+=1
# Create a list with all objects with NC status
nc_list=[]
for i in seq_list_obj:
    if i.status=='NC':
        nc_list.append(i)
# Create a list with all objects with correct status
corr_list=[]
for i in seq_list_obj:
    if i.status=='correct':
        corr_list.append(i)
# Check the Hamming distance between nc_list and corr_list
output_list=[]
for i in nc_list:
    j=0
    while j<len(corr_list):
        if d_h(i.string,corr_list[j].string)==1:
            i.status='incorrect'
            output_list.append([i.string,corr_list[j].string])
            break
        elif d_h(i.string,rev_c(corr_list[j].string))==1:
            i.status='incorrect'
            output_list.append([i.string,rev_c(corr_list[j].string)])
            break
        j+=1
for i in output_list:
    print(f'{i[0]} -> {i[1]}')



    