class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbol_to_number[s[i]] < symbol_to_number[s[i + 1]]:
                total -= symbol_to_number[s[i]]
            else:
                total += symbol_to_number[s[i]]

        return total
