# 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid BST.

def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            #base case
            if not node:
                return True
            #not meet the condition, then return false
            if not (small < node.val < large):
                return False
            # recursively call on the children
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)

            # tree is a BST if left and right subtrees are also BSTs
            return left and right
        # pass the root
        return dfs(root, float("-inf"), float("inf"))