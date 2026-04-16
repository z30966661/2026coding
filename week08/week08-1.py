# LeetCode 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 otherwise
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 不能用 for，因為 n 很大會跑不完
        # 用二分搜尋法，每次縮小一半範圍

        left, right = 1, n + 1  # 左包含、右不包含

        while left < right:
            mid = (left + right) // 2  # 取中間

            if guess(mid) == 0:
                return mid  # 猜對
            if guess(mid) > 0:
                left = mid + 1  # 猜太小，往右
            else:
                right = mid  # 猜太大，往左

        return left
