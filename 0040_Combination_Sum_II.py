class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        T = {}
        for i, j in enumerate(candidates):
            T[(i, j)] = 0

        def rec(n, l):
            for j, i in enumerate(candidates):
                if T[(j, i)] == 0:
                    x = [k for k in l]
                    if n-i == 0:
                        x.append(i)
                        x.sort()
                        if x not in sol:
                            sol.append(x)
                    elif n-i > 0:
                        T[(j, i)] = 1
                        x.append(i)
                        rec(n-i, x)
                        T[(j, i)] = 0
                    else:
                        continue

        rec(target, [])
        return sol
