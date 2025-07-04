def gcdOfStrings(str1: str, str2: str) -> str:
    if not (str1[0] in str2) :
        return ""
    
    else :
        if len(str1) % len(str2) == 0 :
            return min(str1, str2)
        else :
            min_str = min(str1, str2)
            i = len(min_str) // 2
            return min_str[:i]
    
if __name__ == '__main__' :
    str1 = input()
    str2 = input() 
    
    result = gcdOfStrings(str1, str2)
    print(result) 
    