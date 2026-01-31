class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        sumn=(len(nums)*(len(nums)+1))//2
        ans=sumn-sum_nums
        return ans