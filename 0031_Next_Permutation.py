import sys


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        stack = [-1]
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                flag = 1
                break
            stack.append(i)
        if flag == 0:
            # print(8)
            nums = nums.reverse()
            return None
        if nums[i-1] < nums[stack[-1]]:
            x = -1
            while nums[i-1] < nums[stack[-1]]:
                x = stack[-1]
                stack = stack[0:-1]
                if stack == []:
                    break
            nums[i-1], nums[x] = nums[x], nums[i-1]
        else:
            nums[i-1], nums[i] = nums[i], nums[i-1]
        x = nums[:i]
        y = nums[i:]
        y.sort()
        for j in range(i, len(nums)):
            nums[j] = y[j-i]
