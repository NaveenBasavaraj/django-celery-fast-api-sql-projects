# Binary Trees

# Tree is similar to doubly linked list (where nodes are connected with prev and curr pointers), but maintain a
# relationship with other nodes.
# Trees maintain a child parent relations.
# 1. Binary trees have one parent and atmost two child nodes 
# 2. There is only one root node and can have many leaf nodes (at least some are guaranteed)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# Ancestor: A node is an ancestor to all the nodes connected below it.
# Descendent : A child of a node or child of some other descendent of the node

# Depth: no of nodes, from self to all the way up to the root.
# Height: no of nodes, from self to all the way up to the root.

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
    
def insertIntoBst(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insertIntoBst(root.right, val)
    else:
        root.left = insertIntoBst(root.left, val)
    return root

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root