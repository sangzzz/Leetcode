class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sols = set()
        visited = [False for i in range(n)]

        def recurs(visited, l, cnt):
            if cnt == 0:
                sol = []
                for j, i in enumerate(visited):
                    if i:
                        sol.append(j+1)
                sols.add(tuple(sol))
            for i in range(l+1, n+1):
                if visited[i-1]:
                    continue
                visited[i-1] = True
                recurs(visited, i,  cnt - 1)
                visited[i-1] = False
        recurs(visited, 0, k)
        l_sols = []
        for i in list(sols):
            l_sols.append(list(i))
        return l_sols
