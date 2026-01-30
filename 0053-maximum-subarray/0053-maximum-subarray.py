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


# BRUTE FORCE APPROACH
'''
arr=[5,4,-1,7,8]
#maxSum=-999
maxSum=float('-inf')
for i in range(0,len(arr)):
    curSum=0
    for j in range(i,len(arr)):
        curSum=curSum+arr[j]
        if curSum> maxSum:
            maxSum=curSum
print(maxSum)
'''
    
