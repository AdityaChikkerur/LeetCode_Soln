class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        curSum=0
        for num in nums:
            curSum=curSum + num
            maxSum=max(curSum,maxSum)
            if curSum < 0:
                curSum=0
        return maxSum