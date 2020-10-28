class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0 for _ in range(len(matrix[0]))]
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            maxArea = max(maxArea, self.largestRectangleArea(heights))

        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:

        hstack, pstack, maxArea = [], [], 0
        heights.append(0)

        for i in range(len(heights)):
            last_visited_greater_height_position = float('inf')
            while len(hstack) > 0 and hstack[-1] > heights[i]:
                last_visited_greater_height_position = pstack[-1]
                currArea = (i - pstack.pop()) * hstack.pop()
                maxArea = max(maxArea, currArea)
            if len(hstack) == 0 or heights[i] > hstack[-1]:
                hstack.append(heights[i])
                pstack.append(min(i, last_visited_greater_height_position))

        return maxArea
