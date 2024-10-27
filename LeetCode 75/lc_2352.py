class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        import numpy as np
        from collections import Counter

        grid_t = np.array(grid).T.tolist()
        
        grid = ['_'.join(map(str, arr)) for arr in grid]
        grid_t = ['_'.join(map(str, arr)) for arr in grid_t]

        grid = Counter(grid)
        grid_t = Counter(grid_t)

        ans = sum([grid[key] * grid_t[key] for key in grid])

        return ans