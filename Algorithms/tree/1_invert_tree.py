def invertBinaryTree(root):
    if not root:
        return None
    
    root.left, root.right = root.left, root.right
    
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root