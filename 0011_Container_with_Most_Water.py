class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxval = 0
        i = 0
        j = len(height) - 1
        while i < len(height) and j > i:
            val = min(height[i], height[j])*(j-i)
            if val > maxval:
                maxval = val
            if height[j] < height[i]:
                j = j - 1
            else:
                i = i + 1
        return maxval
