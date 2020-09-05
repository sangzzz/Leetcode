
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        points = [(newInterval[0], 0), (newInterval[1], 1)]
        for i in intervals:
            points.append((i[0], 0))
            points.append((i[1], 1))
        points.sort()
        stack = []
        sol = []
        for i in points:
            if i[1] == 0:
                stack.append(i[0])
            else:
                start = stack[-1]
                stack = stack[0:-1]
                end = i[0]
                if len(stack) == 0:
                    sol.append([start, end])
        return sol
