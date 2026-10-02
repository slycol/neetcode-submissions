class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        letters["a"]=0
        letters["b"]=0
        letters["c"]=0
        letters["d"]=0
        letters["e"]=0
        letters["f"]=0
        letters["g"]=0
        letters["h"]=0
        letters["i"]=0
        letters["j"]=0
        letters["k"]=0
        letters["l"]=0
        letters["m"]=0
        letters["n"]=0
        letters["o"]=0
        letters["p"]=0
        letters["q"]=0
        letters["r"]=0
        letters["s"]=0
        letters["t"]=0
        letters["u"]=0
        letters["v"]=0
        letters["w"]=0
        letters["x"]=0
        letters["y"]=0
        letters["z"]=0
        for i in range(len(s)):
            letters[s[i]]+=1
        for j in range(len(t)):
            letters[t[j]]-=1
        for value in letters.values():
            if value!=0:
                return False
        return True
        
            
