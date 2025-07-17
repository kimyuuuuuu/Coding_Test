def reverseVowels(s: str) -> str: 
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'O', 'U', 'E']
    input_vowel = []
    index = []
    
    for i in range(len(s)) :
        if s[i] in vowel :
            input_vowel.append(s[i])
            index.append(i)
    
    # print(input_vowel)
    # print(index)

    input_vowel.reverse()
    
    # print(input_vowel)
    
    s = list(s)
    for i in range(len(index)) :
        s[index[i]] = input_vowel[i]
    
    return ''.join(s)

    
if __name__ == '__main__' :
    s = input()
    results = reverseVowels(s)
    
    print(results)
    