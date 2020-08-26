class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
        except:
            return [-1, -1]
