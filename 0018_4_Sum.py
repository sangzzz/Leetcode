class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums) - 1):
                left = 0
                right = len(nums) - 1
                while i > left and i < right and j > left and j < right:
                    x = nums[i] + nums[left] + nums[right] + nums[j]
                    if x < target:
                        left += 1
                    elif x > target:
                        right -= 1
                    else:
                        s = [nums[left], nums[i], nums[j], nums[right]]
                        if s not in sol:
                            sol.append(s)
                        left += 1
                        right -= 1
        return sol
