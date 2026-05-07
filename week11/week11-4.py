# week11-4.py 學習計畫 Binary Search Tree 最後1題
# LeetCode 450. Delete Node in a BST 把某個node殺掉，再找到繼承者, 放在格子裡
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root): # 找到左子樹最右邊那個人（最強的）
            if root.right: # 右邊還有！
                return findRightest(root.right) # 繼續往右走
            return root # 沒有右邊，那就「你」自己上

        if root == None: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # 找到了！要殺掉 root
            if not root.left: return root.right # 只有右邊，右邊頂替
            if not root.right: return root.left # 只有左邊，左邊頂替
            # 有兩個小孩，找左子樹最強的人來
            successor = findRightest(root.left)
            root.val = successor.val # 篡位
            root.left = self.deleteNode(root.left, successor.val) # 殺掉原本那個人

        return root
