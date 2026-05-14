# week12-3.py 學習計畫 Graph - DFS
# LeetCode 547. Number of Provinces 想知道有幾群是相連的
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected) # 先知道有幾個 Nodes
        visited = set() # 走過的地方，不要再走

        def helper(now):
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)

        ans = 0
        for i in range(N):
            if i not in visited:
                ans += 1
                helper(i)
        return ans
