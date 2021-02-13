class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def traversal(string):
            x = 0
            traverse = []
            for i in string:
                x += 1
                if i == c:
                    traverse = traverse + [_ for _ in range(x-1, 0, -1)] + [0]
                    x = 0
            if x!=0:
                traverse = traverse + [_ for _ in range(1, x+1, 1)]
            return traverse
        goRight = traversal(s)
        goLeft = traversal(s[::-1])[::-1]
        ans = [min(goRight[i], goLeft[i]) for i in range(0, len(s))]
        return ans
    
                
                