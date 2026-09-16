# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        direction=1
        deq=collections.deque([root])
        res=[]
        while deq:
            level=[]
            for i in range(len(deq)):
                node=deq.popleft()
                if node:
                    level.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
            if level:
                    if direction%2==0:
                        res.append(level[::-1])
                    else:
                        res.append(level)
                    direction+=1
        return res