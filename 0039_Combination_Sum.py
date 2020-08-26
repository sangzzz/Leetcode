class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        def rec(n, l):
            for i in candidates:
                x = [j for j in l]
                if n-i == 0:
                    x.append(i)
                    x.sort()
                    if x not in sol:
                        sol.append(x)
                elif n-i > 0:
                    x.append(i)
                    rec(n-i, x)
                else:
                    continue

        rec(target, [])
        return sol
