class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jump = 0
        interval = [0, 0]
        while True:
            jump += 1
            canReach = 0
            for i in range(interval[0], interval[1]+1):
                canReach = max(canReach, i+nums[i])

            if canReach >= len(nums)-1:
                return jump

            interval = [interval[1]+1, canReach]
