
class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """

    def diameterOfBinaryTree(self, root):
        # write your code here
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, node):
        if not node:
            return 0
        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        self.max = max(self.max, left_length + right_length)
        return max(left_length, right_length) + 1

