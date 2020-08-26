class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m = 2**31
        nums.sort()
        x = 0

        for pivot in range(1, len(nums)-1):
            left = 0
            right = len(nums) - 1
            while pivot < right and pivot > left:
                t = nums[left] + nums[pivot] + nums[right]
                if t > target:
                    right -= 1
                elif t < target:
                    left += 1
                else:
                    return target
                if abs(t-target) < m:
                    m = abs(t-target)
                    x = t
        return x
