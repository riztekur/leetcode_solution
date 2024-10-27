class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        my_dict = dict(Counter(arr))

        return len(my_dict.values()) == len(set(my_dict.values()))