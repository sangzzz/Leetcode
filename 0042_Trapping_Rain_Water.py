class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0
        lmax = 0
        rmax = 0
        i = 0
        j = len(height) - 1
        vol = 0
        while i <= j:
            lmax, rmax = max(lmax, height[i]), max(rmax, height[j])
            if lmax <= rmax:
                vol += lmax - height[i]
                i += 1
            else:
                vol += rmax - height[j]
                j -= 1
        return vol
