class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []

        def p(i, sol):
            if len(sol) == len(nums):
                perm.append(sol)
            for x in range(0, len(i)):
                if x == len(i)-1:
                    p(i[0:-1], sol+[i[x]])
                else:
                    p(i[0: x] + i[x+1:], sol+[i[x]])
        p(nums, [])
        return perm
