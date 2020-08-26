class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = {}
        if nums == []:
            return -(2**31)
        maximum[0] = nums[0]
        M = maximum[0]
        for i in range(1, len(nums)):
            maximum[i] = nums[i]
            maximum[i] = max(maximum[i-1]+nums[i], nums[i])
            if maximum[i] > M:
                M = maximum[i]
        return M
