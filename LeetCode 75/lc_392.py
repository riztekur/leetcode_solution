class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i = i + 1
            j = j + 1
        
        return i == len(s)