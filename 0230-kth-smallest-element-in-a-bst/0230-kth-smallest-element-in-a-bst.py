# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.inorder(root,res)
        return res[k-1]

    def inorder(self,curr,res):
        if curr is None:
            return 
        self.inorder(curr.left,res)
        res.append(curr.val)
        self.inorder(curr.right,res)