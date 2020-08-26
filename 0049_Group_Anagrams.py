class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        T = {}
        for i in range(len(strs)):
            letters = [j for j in strs[i]]
            letters.sort()
            if tuple(letters) not in T:
                T[tuple(letters)] = [strs[i]]
            else:
                T[tuple(letters)] += [strs[i]]
        sol = []
        for i in T:
            sol.append(T[i])
        # print(T)
        return sol
