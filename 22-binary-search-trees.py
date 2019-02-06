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

    def getHeight(self, root):
        heightSubTreeLeft = 0
        heightSubTreeRight = 0

        if (root.right == None and root.left == None):
            return 0

        if (root.right != None):
            heightSubTreeRight = 1 + self.getHeight(root.right)

        if (root.left != None):
            heightSubTreeLeft = 1 + self.getHeight(root.left)

        if heightSubTreeLeft > heightSubTreeRight:
            return heightSubTreeLeft
        
        return heightSubTreeRight
        


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
