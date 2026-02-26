#week01-1.py
# 練習從 0 到 n-1 問有幾個偶數
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s, 2)
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n + 1
            ans += 1
        return ans
