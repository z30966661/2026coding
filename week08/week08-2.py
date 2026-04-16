# week08-2.py 猜數字題 Binary Search 第1題

# 給你 guess() 你可以呼叫它，找出 1...n 裡面的「答案」
class Solution:
    def guessNumber(self, n: int) -> int:

        # 方法1：暴力法（不推薦，會超時）
        # for i in range(n+1): print(-guess(i), end=' ')
        # return bisect.bisect(range(n+1), 0, key=lambda x: guess(x))

        # 方法2：Binary Search（重點）
        left, right = 1, n + 1  # 左包含、右不包含

        while left < right:
            mid = (left + right) // 2  # 中間值

            if guess(mid) == 0:
                return mid  # 猜對

            if guess(mid) > 0:
                left = mid + 1  # 猜太小 → 往右
            else:
                right = mid  # 猜太大 → 往左

        return left


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 otherwise
# def guess(num: int) -> int:
