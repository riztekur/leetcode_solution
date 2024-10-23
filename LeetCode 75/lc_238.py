class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer