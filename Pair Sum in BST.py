'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def findTarget(self, root, target): 
        # Inorder traversal se sorted array bana lenge
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.data)
            inorder(node.right, arr)
        
        arr = []
        inorder(root, arr)  # BST ka inorder sorted hoga
        
        # Ab do pointer se check karenge sum == target
        left = 0
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True  # Pair mil gaya
            elif current_sum < target:
                left += 1    # Chhota sum, to left pointer aage badhao
            else:
                right -= 1   # Bada sum, to right pointer peeche lao
        
        return False  # Koi pair nahi mila
