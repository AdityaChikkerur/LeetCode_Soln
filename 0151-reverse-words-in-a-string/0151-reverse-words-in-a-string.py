class Solution:
    def reverseWords(self, s: str) -> str:
        str=[]
        str=s.split()
        str=str[::-1]
        str=" ".join(str)
        return str
        