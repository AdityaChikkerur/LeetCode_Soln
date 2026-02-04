class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=[0]*len(height)
        r_max=[0]*len(height)
        ans=0
        #left
        l_max[0]=height[0]
        for i in range(1,len(height)):
            l_max[i]=max(l_max[i-1],height[i])
       # print(l_max)
        #right
        r_max[(len(height)-1)]=height[-1]  # len(height) -1 (negative indexing)
        for i in range(len(height)-2,-1,-1):
            r_max[i]=max(height[i],r_max[i+1])
        print(r_max)

        for i in range(1,len(height)):
            ans=ans + (min(l_max[i],r_max[i]) - height[i])
        return ans

