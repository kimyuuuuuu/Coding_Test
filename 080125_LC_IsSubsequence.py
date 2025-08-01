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
            
        if read2 < len(t) :
            read1 += 1
            read2 += 1
            
        else :
            break
        
    return read1 == len(s)
    

if __name__ == '__main__' :
    s = input()
    t = input() 
    
    print(isSubsequence(s, t))
    
# 1.  "b", "c" 인 경우 => 두 번째 while 문을 돌 수 없음 
#      => 맨 처음에 한자리 문자열 걸러내도록 함
# 2. 논리적 오류 발생
#    => read1, 2를 언제 증가시켜야하는지 고민할 것