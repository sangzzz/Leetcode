class Solution:
    def intToRoman(self, num: int) -> str:
        assert 1 <= num <= 3999
        units = num % 10
        tens = (num//10) % 10
        hunds = ((num//10)//10) % 10
        thousands = (((num//10)//10)//10) % 1000
        strunits = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',
                    5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        strtens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
                   5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        strhuns = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD',
                   5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        strthou = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}

        ans = strthou[thousands] + strhuns[hunds] + \
            strtens[tens] + strunits[units]

        return ans
