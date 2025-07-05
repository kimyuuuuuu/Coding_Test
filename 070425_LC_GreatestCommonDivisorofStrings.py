def gcdOfStrings(str1: str, str2: str) -> str:
    if not (str1[0] in str2) :
        return ""
    
    else :  
        str = min(str1, str2)
        len1, len2 = len(str1), len(str2)
        
        for i in range(len(str), 0, -1) :
            base = str[:i]
            len_base = len(base)
            
            # if (len1 % len_base == 0) and ( len2 % len_base == 0):  
            if ((base * (len1 // len_base)) in str1) and ((base * (len2 // len_base)) in str2) :
                return base
            else :
                return ""


if __name__ == '__main__' :
    str1 = input()
    str2 = input() 
    
    result = gcdOfStrings(str1, str2)
    print(result) 
    
# 1. misunderstand (같은 문자가 반복되는 열만 나오는 줄 알았음)
# 2. 짝수/홀수의 경우 나누어 떨어지지 않기 때문에 base가 문자열에 있는지 뿐만 아니라, 나누어 떨어지는지도 확인해야함 
#    wrong answer - if (base in str1) and (base in str2) : return base
# 3. 나누어 떨어지는지 뿐만 아니라 같은 문자열로 이루어져있는지 봐야함
#    wrong answer - if (base in str1) and (base in str2) and (len(str1) % len(base) == 0) and (len(str2) % len(base) == 0): return base
# 4. Key point : 정답 K가 1) 두 문자열에 있어야 함 2) 두 문자열을 나눈 후 나머지가 없어야 함 3) 그 안에 K로만 이루어져 있어야 함 
