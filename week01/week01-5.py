#week01-5.py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        preSum = [1]
        postSum = [1]

        # «eºó­¼¿n
        for i in range(N):
            preSum.append(preSum[-1] * nums[i])

        # «áºó­¼¿n
        for i in range(N):
            postSum.append(postSum[-1] * nums[N-1-i])

        ans = []
        for i in range(N):
            ans.append(preSum[i] * postSum[N-1-i])

        return ans
