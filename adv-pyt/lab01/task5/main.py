"""
Maksymilian Wiśniewski
Task5 : Longest Common Prefix

"""

# Brute force approach
# O(n*k) where n is no. strings and k the maximum lenght

def common_prefix(string_table):
    res = ""
    for i in range(len(string_table[0])):
        for s in string_table:
            if i == len(s) or s[i] != string_table[0][i]:
                return res
        res+= string_table[0][i]

    return res


# Finding the longest common prefix using trie data structure
# we're adding each word to the dictionary, that is implemented by a tree with, letters in nodes
# if the node has more than 1 children we end our search returning current depth
# when there are no children that means we should immediately return current depth

# Time complexity:
#                   O(#strings * max len) - for buiilding trie

class Node:
    def __init__(self):
        self.isLeaf = False
        self.children = {}

def insert(head, s):
    curr = head
    
    for c in s:
        curr = curr.children.setdefault(c, Node())
    
    curr.isLeaf = True

def Find(string_table):
    head = Node()
    
    for s in string_table:
        print(head.children, end="\n")
        insert(head, s)
    
    answer = ""
    curr = head
    
    while curr and not curr.isLeaf and len(curr.children) == 1:
        for k, v in curr.children.items():
            answer += k
            curr = v
    
    return answer



if __name__ == "__main__":
    pass