from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1 = Counter(word1)
        word2 = Counter(word2)

        if set(word1.keys()) != set(word2.keys()):
            return False

        return sorted(word1.values()) == sorted(word2.values())
