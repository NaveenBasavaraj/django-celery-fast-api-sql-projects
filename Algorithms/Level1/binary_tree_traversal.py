from binary_search_tree import TreeNode

class BinaryTree:
    # left prioritizing
    # left - root - right
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
    
    def preorder(self, root):
        # left prioritizing
        # root - left - right
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        # left prioritizing
        # left - right - root
        if not root:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
        
        