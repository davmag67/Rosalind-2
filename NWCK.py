# Important assumption:
# This exercise is asking the distances between any nodes of the tree, which means including also the internal nodes.
# The assumption is that all nodes must have a label. The exception will be just the root node.
# In case we need to assume that some of the internal nodes will have no label. The approach will be a little different
# and will be the same approach I used with the other exercise: NKEW.
# In any case we need to assume that the leaves will have labels.
################################################################################################
# Assuming the input data are strings in the format shown in the NWCK_file.txt
in_nwck_list=[] # List of the n strings
in_nodes=[] # List of n couples of nodes
# Import the file in a clean list
with open('NWCK_file.txt') as file:
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
#############################################################################
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
##############################################################################
# Rewrite the in_nodes in a list of couples lists
nodes_list=[]
for s in in_nodes:
    nodes_list.append(split(s))
###############################################################################
# The position of a node, compared to the root, depends on the number and type of parenthesis
# between the node and the root.
#############################################################################
# Function that calculates the edges from a node to the root
# The number of edges is the net result of the ')' minus the '(' between the node and the root
def node_root(tree, node):
    start=tree.index(node)+len(node)
    count=0
    for i in range(start,len(tree)):
        if tree[i]==')':
            count+=1
        elif tree[i]=='(':
            count-=1
        else:
            pass
    return count
# Function that provides the parent node of a given node.
# The parent node will be right after the next parenthesis ')' not considering those parenthesis couple '(' and ')' that 
# may open and close before the parent one. To consider them I used a counter that may increase or decrease depending
# on the sequence of parenthesis encountered.
def parent(tree,node):
    start=tree.index(node)+len(node)
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
    parent_node_start=i+1
    parent_node=''
    j=parent_node_start
    while j<len(tree):
        if tree[j]!='(' and tree[j]!=')' and tree[j]!=',' and tree[j]!=';':
            parent_node=parent_node+tree[j]
            j+=1
        else:
            break
    return parent_node
# Function that calculates the path distance between two nodes in the specific case 
# they are at the same distance from the root.
def dist_eq(tree,node1,node2):
    count=0
    if node1==node2:
        return count
    else:
        p1=node1
        p2=node2
        while True:
            p1=parent(tree,p1)
            p2=parent(tree,p2)
            count+=2
            if p1==p2:
                break
            else:
                if p1.endswith(';') or p2.endswith(';'):
                    raise Exception('No path found')
                    break
                else:
                    pass
    return count
###################################################################################
# Function that calculates the path distance between two any nodes of a tree
def dist(tree,node1,node2):
    count=0
    d1=node_root(tree,node1)
    d2=node_root(tree,node2)
    if d1==d2:
        count=dist_eq(tree,node1,node2)
    else:
        if d1<d2:
            count=d2-d1
            delta=d2-d1
            p2=node2
            while delta!=0:
                p2=parent(tree,p2)
                delta-=1
            count=count+dist_eq(tree,node1,p2)
        else:
            count=d1-d2
            delta=d1-d2
            p1=node1
            while delta!=0:
                p1=parent(tree,p1)
                delta-=1
            count=count+dist_eq(tree,p1,node2)
    return count
##################################################################################
output_list=[]
for i in range(len(in_nwck_list)):
    output_list.append(dist(in_nwck_list[i],nodes_list[i][0],nodes_list[i][1]))
output=''
for j in output_list:
    output=output+str(j)+' '
print(output)

        
            

        
    
    
        