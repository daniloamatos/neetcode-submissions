# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

        curr = root
        parent = None
        father = None

        while curr:
            if key < curr.val:
                parent = curr
                curr = curr.left

            elif key > curr.val:
                parent = curr
                curr = curr.right

            else:
                # Dois filhos
                if curr.left and curr.right:
                    temp = curr
                    father = curr
                    curr = curr.right

                    while curr.left:
                        father = curr
                        curr = curr.left

                    temp.val = curr.val

                    if father.left == curr:
                        father.left = curr.right
                    else:
                        father.right = curr.right

                # Zero ou um filho
                else:
                    temp = curr.left or curr.right

                    if parent.left == curr:
                        parent.left = temp
                    else:
                        parent.right = temp

                break

        return root
        # if not root:
        #     return None
            
        # if root.val == key:
        #     if not root.left:
        #         return root.right
        #     if not root.right:
        #         return root.left

        # if root.val == key:
        #     if not root.left:
        #         return root.right
        #     if not root.right:
        #         return root.left

        #     father = root
        #     curr = root.right

        #     while curr.left:
        #         father = curr
        #         curr = curr.left

        #     root.val = curr.val

        #     if father == root:
        #         father.right = curr.right
        #     else:
        #         father.left = curr.right

        #     return root
        # curr = root
        # parent = None
        # father = None
        # while curr:

        #     if key == curr.val:
        #         if not curr.left and not curr.right:
        #             if parent.left == curr:
        #                 parent.left = None
        #                 break
        #             else:
        #                 parent.right = None
        #                 break
        #         elif not curr.left:
        #             if parent.left == curr:
        #                 parent.left = curr.right
        #                 break
        #             else:
        #                 parent.right = curr.right
        #                 break
        #         elif not curr.right:
        #             if parent.left == curr:
        #                 parent.left = curr.left
        #                 break
        #             else:
        #                 parent.right = curr.left
        #                 break
        #         else:
        #             temp = curr
        #             curr = curr.right
        #             while curr.left:
        #                 father = curr
        #                 curr = curr.left
        #             if parent.left == temp:
        #                 parent = parent.left
        #                 parent.val = curr.val
        #                 parent.right = None
        #                 break
        #             else:
        #                 parent = parent.right
        #                 parent.val = curr.val
        #                 parent.right = None
        #                 break

        #     elif key > curr.val:
        #         parent = curr
        #         curr = curr.right
        #     else:
        #         parent = curr
        #         curr = curr.left


        # return root


