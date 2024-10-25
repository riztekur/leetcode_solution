class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if min(nums) == 1:
            return len(nums)-1

        k = 1

        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k = k - 1
            if k < 0:
                if nums[left] == 0:
                    k = k + 1
                left = left + 1
                
        return right - left