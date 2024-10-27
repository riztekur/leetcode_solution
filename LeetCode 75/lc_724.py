class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = sum(nums[0:0])
        right_sum = sum(nums[1:len(nums)])

        if left_sum == right_sum:
            return 0

        for i in range(1,len(nums)):
            left_sum = left_sum + nums[i-1]
            right_sum = right_sum - nums[i]

            if left_sum == right_sum:
                return i
        
        return -1