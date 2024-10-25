class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','i','u','e','o']
        s = [1 if x in vowels else 0 for x in s]
        
        ans = current_sum = sum(s[:k])

        for i in range(k, len(s)):
            current_sum = current_sum + (s[i] - s[i - k])
            ans = max(ans, current_sum)
        return ans