def gcdOfStrings(str1: str, str2: str) -> str:
    if not (str1[0] in str2) :
        return ""
    
    else :
        str = min(str1, str2)
        len1, len2 = len(str1), len(str2)
        
        for i in range(len(str), 0, -1) :
            base = str[:i]
            len_base = len(base)
            
            if (len1 % len_base == 0) and ( len2 % len_base == 0):
                if ((base * (len1 // len_base)) in str1) and ((base * (len2 // len_base)) in str2) :
                    return base
                else :
                    return ""


if __name__ == '__main__' :
    str1 = input()
    str2 = input() 
    
    result = gcdOfStrings(str1, str2)
    print(result) 
    