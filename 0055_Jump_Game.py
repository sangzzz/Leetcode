class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        interval = [0, 0]
        while True:
            canReach = 0
            for i in range(interval[0], interval[1]+1):
                canReach = max(canReach, i+nums[i])

            if canReach == interval[1]:
                return False

            if canReach >= n-1:
                return True

            interval[0] = interval[1] + 1
            interval[1] = canReach
