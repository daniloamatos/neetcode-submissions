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
            if val > curr.val:
                if val > curr.val:
                    if r:
                        curr = r
                        l = curr.left
                        r = r.right
                    else:
                        curr.right = TreeNode(val)
                        break
                else:
                    if l:
                        curr = l
                        l = l.left
                        r = curr.right
                    else:
                        curr.left = TreeNode(val)
                        break
            else:
                if val > curr.val:
                    if r:
                        curr = r
                        l = curr.left
                        r = r.right
                    else:
                        curr.right = TreeNode(val)
                        break
                else:
                    if l:
                        curr = l
                        l = l.left
                        r = curr.right
                    else:
                        curr.left = TreeNode(val)
                        break

        return root