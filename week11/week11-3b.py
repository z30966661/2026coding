#week11-5.py
#450. Delete Node in a BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root):
            if root.right:
                return findRightest(root.right)
            return root
        if root == None:
            return root
        if root.val == key:
            if root.left:
                now = findRightest(root.left)
                root.val = now.val
                root.left = self.deleteNode(root.left, now.val)
            else:
                return root.right
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
