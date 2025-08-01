def isSubsequence(s: str, t: str) -> bool:
    read1 = 0
    read2 = 0
    
    if len(s) == 1 and len(t) == 1 :
        if s[read1] == t[read2] :
            return True
        else :
            return False
    
    while read1 < len(s) and read2 < len(t):
        current = s[read1] 
        
        while read2 < len(t) and t[read2] != current  :
            read2 += 1 

        read1 += 1
        
    if read1 == len(s) :
        return True 
        
    else :
        return False
    

if __name__ == '__main__' :
    s = input()
    t = input() 
    
    print(isSubsequence(s, t))
    
# "b", "c" 인 경우 