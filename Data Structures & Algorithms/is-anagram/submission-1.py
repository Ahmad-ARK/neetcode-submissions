class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen  = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1

        
        for char in t:
            seen[char] = seen.get(char, 0) - 1

        isAnagram = False

        for key in seen:
            if seen[key] == 0:
                isAnagram = True
            else:
                isAnagram = False
        return isAnagram

            
