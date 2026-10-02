class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        acceptable =   {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"}
        for char in s:
            if char not in acceptable:
                s = s.replace(char,"")
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True