class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        curSum=0
        for num in nums:
            curSum=curSum + num
            if curSum >  maxSum:
                maxSum=curSum
    return maxSum