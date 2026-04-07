class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        
        # count frequency of each character in s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # subtract frequency of each character in t
        for char in t:
            count[char] = count.get(char, 0) - 1
            
        # if all values are 0, every character balanced out
        for val in count.values():
            if val != 0:
                return False
                
        return True