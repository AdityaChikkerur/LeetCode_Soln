class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[0]*100
        for i in range(0,len(s)):
            substr=""
            for j in range(i,len(s)):
                if s[j] not in substr:
                    substr=substr + s[j]
                else:
                    break
            a.append(len(substr))
        return max(a)
                




                
                  