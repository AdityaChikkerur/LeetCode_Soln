# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        level=[]
        q=deque()
        q.append(root)
        q.append(None)

        if root is None:
            return []
       
        while q:
            curr=q.popleft()
            if curr is None:
                res.append(level)
                level=[]
                if q:
                    q.append(None)
                else:
                    break
            else:
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res