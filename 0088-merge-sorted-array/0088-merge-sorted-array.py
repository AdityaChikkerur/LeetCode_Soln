class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # for i in range(0,m):
        for j in range(0,n):        
            nums1.append(nums2[j])
            nums1.sort()
        # print(nums1)
                 
        
        # for i in range(0,m):
            if 0 in nums1:
                nums1.remove(0)
        print(nums1)

        