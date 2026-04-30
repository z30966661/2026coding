# week10-6.py 學習計畫 Binary Tree - DFS 第5題
# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 找到中間 ZigZag 左右左右 or 右左右左 最長的那一個

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 整個的答案

        def helper(root):
            if root == None:
                return 0, 0 # 左邊最長、右邊最長

            # 遞迴得到小孩的左邊最長、右邊最長路徑
            Lans1, Lans2 = helper(root.left)
            Rans1, Rans2 = helper(root.right)

            # 當前節點往左走，必須接小孩「往右」的長度；往右走則接小孩「往左」
            cur_left = Lans2 + 1
            cur_right = Rans1 + 1

            # 更新全局最大值
            self.ans = max(self.ans, cur_left, cur_right)

            return cur_left, cur_right

        helper(root)
        return self.ans - 1 # 減 1 是因為題目要求的是「邊」的數量而非節點數
