"""
Ms. Namasivayam
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node


'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
    tempString = ""
    if (root == None):
        return tempString
    tempString += str(getInorder(root.left))
    tempString += str(root.val) + '-'
    tempString += str(getInorder(root.right))
    return tempString









'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
    tempString = ""
    if (root == None):
        return tempString
    tempString += str(getPostorder(root.left))
    tempString += str(getPostorder(root.right))
    tempString += str(root.val) + '-'
    return tempString



'''
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getPreorder(root):
    tempString = ""
    if (root == None):
        return tempString
    tempString += str(root.val) + '-'
    tempString += str(getPreorder(root.left))
    tempString += str(getPreorder(root.right))
    return tempString


'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''
def insert(root, key):
    keyNode = Node(key)

    if (root.val == key):
        return root

    else:
        if(key < root.val):
            if(key < root.val and root.left == None):
                root.left = keyNode
                return root
            elif(key >= root.val and root.right == None):
                root.right = keyNode
                return root
            insert(root.left, key)

        elif(key >= root.val):
            if (key < root.val and root.left == None):
                root.left = keyNode
                return root
            elif (key >= root.val and root.right == None):
                root.right = keyNode
                return root
            insert(root.right, key)

    return root












'''
Challenge: A function determines if a binary tree 
is a valid binary search tree
'''
def isBST(root):
    return False


if __name__ == '__main__':
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

