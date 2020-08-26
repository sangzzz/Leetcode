class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # l = 0
        # h = len(nums)-1
        # m = (l+h)//2
        if target > nums[-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0

        try:
            return nums.index(target)
        except:
            l = 0
            r = len(nums) - 1
            m = (l+r)//2
            while l < r+1:
                m = (l+r)//2
                if m == len(nums)-1:
                    return len(nums)
                if nums[m] < target and nums[m+1] > target:
                    return m+1
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return 0

    def find_left(self, nums, left, right, target):
        m = (left + right)//2
        while left < right+1:
            m = (left+right)//2
            if nums[m] < target:
                left = m + 1
            elif nums[m-1] < target:
                return m
            else:
                right = m - 1
        return left
