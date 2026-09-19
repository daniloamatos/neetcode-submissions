class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = root
        result = []
        stack = []

        while tree or stack:
            while tree:
                stack.append(tree)
                tree = tree.left
            tree = stack.pop()
            result.extend({tree.val})
            tree = tree.right

        return result