# Important assumption:
# In this exercise (given the sample dataset) I am assuming that the internal nodes may have no labels.
# Therefore the approach will be a little different compared to the one I did for the exercise NWCK.
# I will use as node labels the nodes positions within the tree Newick string.
# For the internal nodes I will consider the position of the parenthesis ')'
################################################################################################
# Assuming the input data are strings in the format shown in the NKEW_file.txt
in_nwck_list=[] # List of the n strings
in_nodes=[] # List of n couples of nodes
# Import the file in a clean list
with open('NKEW_file.txt') as file:
    file_lines=(file.readlines())
    file_lines_clean=[]
    for a in file_lines:
        file_lines_clean.append(a.rstrip())
# Population of input lists
for i in range(0,len(file_lines_clean),3):
    in_nwck_list.append(file_lines_clean[i])
for j in range(1,len(file_lines_clean),3):
    in_nodes.append(file_lines_clean[j])
# Check the lenght of the trees list
if len(in_nwck_list)>40:
    raise Exception('The number of trees cannot be higher than 40')
# The number of nodes in a tree is equal to the number of ')' plus the number of ',' in the Newick string plus 1
# Definition of the function that calculates the number of nodes of the tree.
def num_nodes(t):
    count=1
    for i in t:
        if i==')' or i==',':
            count+=1
        else:
            pass
    return count
# Check the max number of nodes in all trees
node_count_list=[]
for i in in_nwck_list:
    node_count_list.append(num_nodes(i))
if max(node_count_list)>200:
    raise Exception('the trees must have max 200 nodes')
###########################################################################
# Definition of a function that take a string with a blank char and split it in two strings and put them in a list
def split(s):
    s1=''
    s2=''
    i=0
    while i<len(s):
        if s[i]!=' ':
            s1=s1+s[i]
            i+=1
        else:
            for j in range(i+1,len(s)):
                s2=s2+s[j]
            break
    return [s1,s2]
#######################################################################################
# Rewrite the in_nodes in a list of couples lists
nodes_list=[]
for s in in_nodes:
    nodes_list.append(split(s))
###############################################################################
# The position of a node, compared to the root, depends on the number and type of parenthesis
# between the node and the root.
###############################################################################
# Function that calculates the edges from a node to the root. In this case the identification of the nodes will be with 
# their position in the tree Newick string.
# The number of edges is the net result of the ')' minus the '(' between the node and the root
def node_root(tree, node_pos):
    start=node_pos+1
    count=0
    for i in range(start,len(tree)):
        if tree[i]==')':
            count+=1
        elif tree[i]=='(':
            count-=1
        else:
            pass
    return count
# Function that provides the parent node of a given node. In this case the identification of the nodes will be with 
# their position in the tree Newick string.
# The parent node will correspond with the position number of the next parenthesis ')' not considering those parenthesis 
# couples '(' and ')' that may open and close before the parent one. To consider them I used a counter that may increase or 
# decrease depending on the sequence of parenthesis encountered.
# The function will return the position of the parenthesis corresponding to the parent node.
def parent(tree,node_pos):
    start=node_pos+1
    count=0
    i=start
    while i<len(tree):
        if tree[i]==')':
            count+=1
        elif tree[i]=='(':
            count-=1
        else:
            pass
        if count==1:
            break
        else:
            i+=1
    parent_node_pos=i
    return parent_node_pos
# Definition of a function that takes a node position and returns the edge weight associated.
# I am assuming that the weight number is a sequence of integers.
def weig(tree,node_pos):
    start=node_pos+1
    i=start
    weight=''
    while i<len(tree):
        if tree[i]==':':
            j=i+1
            nums=('1','2','3','4','5','6','7','8','9','0')
            while tree[j] in nums:
                weight=weight+tree[j]
                j+=1
            break
        else:
            i+=1
    if weight=='':
        weight=0
    weight=int(weight)
    return weight
# Function that calculates the weight path distance between two nodes in the specific case 
# that they are at the same distance from the root.
# Also in this case the inputs will be the nodes positions in the Newick string.
def dist_eq(tree,node_pos1,node_pos2):
    count=0
    if node_pos1==node_pos2:
        return count
    else:
        pos1=node_pos1
        pos2=node_pos2
        while True:
            count=count+(weig(tree,pos1))+(weig(tree,pos2))
            pos1=parent(tree,pos1)
            pos2=parent(tree,pos2)
            if pos1==pos2:
                break
            else:
                if tree[pos1+1]==';' or tree[pos2+1]==';':
                    raise Exception('No path found')
                    break
                else:
                    pass
    return count
# Function that calculates the path distance between two nodes of a tree
def dist(tree,node_pos1,node_pos2):
    count=0
    d1=node_root(tree,node_pos1)
    d2=node_root(tree,node_pos2)
    if d1==d2:
        count=dist_eq(tree,node_pos1,node_pos2)
    else:
        if d1<d2:
            delta=d2-d1
            pos2=node_pos2
            count=0
            while delta!=0:
                count=count+weig(tree,pos2)
                pos2=parent(tree,pos2)
                delta-=1
            count=count+dist_eq(tree,node_pos1,pos2)
        else:
            delta=d1-d2
            pos1=node_pos1
            while delta!=0:
                count=count+weig(tree,pos1)
                pos1=parent(tree,pos1)
                delta-=1
            count=count+dist_eq(tree,pos1,node_pos2)
    return count
############################################################################
output_list=[]
for i in range(len(in_nwck_list)):
    output_list.append(dist(in_nwck_list[i],in_nwck_list[i].index(nodes_list[i][0]),in_nwck_list[i].index(nodes_list[i][1])))
output=''
for j in output_list:
    output=output+str(j)+' '
print(output)







