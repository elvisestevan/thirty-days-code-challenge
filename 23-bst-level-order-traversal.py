import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = []
        queue.insert(0, root)
        
        while len(queue) > 0:
            value = queue.pop()
            print(value.data, end=' ')
            if (value.left != None):
                queue.insert(0, value.left)
            if (value.right != None):
                queue.insert(0, value.right)
            
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

