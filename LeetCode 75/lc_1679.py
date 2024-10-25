class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        left = 0
        right = len(nums)-1
        ans = 0

        while left < right:
            if nums[left] + nums[right] == k:
                left = left + 1
                right = right - 1
                ans = ans + 1
            elif nums[left] + nums[right] < k:
                left = left + 1
            else:
                right = right - 1
        return ans