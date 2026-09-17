# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        l = root.left if root.left else None
        r = root.right if root.right else None
        curr = root
        while curr:
            direction = "right" if val > curr.val else "left"
            next_node = getattr(curr, direction)

            if next_node:
                curr = next_node
                l = curr.left
                r = curr.right
            else:
                setattr(curr, direction, TreeNode(val))
                break

        return root