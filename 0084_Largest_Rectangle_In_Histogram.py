class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # DYNAMIC PROGRAMMING --> Elegant, but O(n^2)
        # T = [[0 for i in range(len(heights))] for _ in range(len(heights))]
        # max_area = 0
        # for j, i in enumerate(heights):
        #     T[j][j] = heights[j]
        #     if i>max_area:
        #         max_area = i
        # for i in range(1, len(heights)):
        #     for j in range(0, len(heights)-i):
        #         T[j][j+i] = min(T[j][j+i-1], T[j+1][j+i])
        #         if T[j][j+i]*(i+1)>max_area:
        #             max_area = T[j][j+i] * (i+1)
        # return max_area

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
