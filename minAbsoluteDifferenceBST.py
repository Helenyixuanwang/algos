# 530. Minimum Absolute Difference in BST

# Given the root of a BST, return the minimum absolute difference between the values of any two different nodes in the tree.

# Trivia to know: an inorder DFS traversal prioritizing left before right on a BST will handle the nodes in sorted order.

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            # inorder DFS traversal to make a sorted array-- values
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)

        values = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])
        
        return ans