class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = set()

        def recurs(sol, index):
            sols.add(tuple(sol))
            for i in range(index + 1, len(nums)):
                l = len(sol)
                sol.add(nums[i])
                if l+1 == len(sol):
                    recurs(sol, i)
                    sol.remove(nums[i])
        recurs(set(), -1)
        return sols
