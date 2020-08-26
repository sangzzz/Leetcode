class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        i = 0
        j = len(nums)-1

        sol = set()

        nums.sort()

        for pivot in range(1, len(nums)-1):
            left = 0
            right = len(nums) - 1
            while pivot < right and pivot > left:
                target = nums[left] + nums[pivot] + nums[right]
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    sol.add(tuple([nums[left], nums[pivot], nums[right]]))
                    left += 1
                    right -= 1

        return sol
