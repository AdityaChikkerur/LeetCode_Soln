# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # res=[]
        # level=[]
        # c=0
        # q=deque()
        # q.append(root)
        # q.append(None)

        # if root is None:
        #     return 0
       
        # while q:
        #     curr=q.popleft()
        #     if curr is None:
        #         res.append(level)
        #         level=[]
        #         c+=1
        #         if q:
        #             q.append(None)
        #         else:
        #             break
        #     else:
        #         level.append(curr.val)
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        # return c
        if root is None:
            return 0
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)

        return max(left_height,right_height)+1