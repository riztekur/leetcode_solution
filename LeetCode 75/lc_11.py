class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1

        while left < right:
            water = min(height[left],height[right]) * (right-left)
            if water >= max_water:
                max_water = water
            
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1

        return max_water  
        