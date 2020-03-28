from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        depth = (N + 1) / 2
        temp = ['null'] * N

        def nextlevel():
            pass
        return temp


test = Solution()
N = 7
print(test.allPossibleFBT(7))
