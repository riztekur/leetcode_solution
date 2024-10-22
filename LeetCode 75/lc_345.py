class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        pos = []
        vow = []

        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                pos.append(i)
                vow.append(s[i])

        inv_vow = vow[::-1]

        for i in range(len(pos)):
            s[pos[i]] = inv_vow[i]

        return ''.join(s)