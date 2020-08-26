
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = len(words)
        if count == 0:
            return []
        word = Counter(words)
        word_len = len(words[0])
        seq_length = count * word_len
        result = []
        for i in range(0, len(s) - seq_length + 1):
            counter = word.copy()
            valid = True
            for j in range(i, i + seq_length, word_len):
                w = s[j:j + word_len]
                if counter[w] > 0:
                    counter[w] -= 1
                else:
                    valid = False
                    break
            if valid:
                result.append(i)
        return result
