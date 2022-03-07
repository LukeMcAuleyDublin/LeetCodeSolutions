class Solution:
    
    def romanToInt(self, s: str) -> int:
        numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        
        if s == "":
            return 0
        if s in numerals:
            return numerals[s]
        
        prev = None
        total = 0
        for letter in s[::-1]:
            value = numerals[letter]
            if  ((letter == 'I' and prev in ('V', 'X')) or 
                (letter == 'X' and prev in ('L', 'C')) or 
                (letter == 'C' and prev in ('D', 'M'))):
                total -= value
            else:
                total += value
            
            prev = letter
            
        return total
        
        