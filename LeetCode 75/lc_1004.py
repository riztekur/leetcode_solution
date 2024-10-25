class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k = k - 1
            if k < 0:
                if nums[left] == 0:
                    k = k + 1
                left = left + 1
                
        return right - left + 1
