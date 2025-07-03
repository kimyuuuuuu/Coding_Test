def mergeAlternately(word1: str, word2: str) -> str:
    length = min(len(word1), len(word2)) 

    result = []
    
    for i in range(length) :
        result.append(word1[i]) 
        result.append(word2[i])
        
    if len(word1) > len(word2) :
        result.append(word1[length:])
    
    else :
        result.append(word2[length:])
        
    result = ''.join(result)  # **리스트 문자열 합치기 
        
    return result 
    
    
if __name__ == '__main__' :
    word1 = input()
    word2 = input() 
    
    result = mergeAlternately(word1, word2)
    print(result) 
    