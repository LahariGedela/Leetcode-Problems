class Solution:
    def wordPattern(self, pattern: str,s:str)->bool:
        words=s.split()
        if(len(pattern)!=len(words)):
            return False
        c={}
        w={}
        for ch,word in zip(pattern,words):
            if(ch in c):
                if c[ch]!=word:
                    return False
            else:
                c[ch]=word
            if(word in w):
                if w[word]!=ch:
                    return False
            else:
                w[word]=ch
        return True