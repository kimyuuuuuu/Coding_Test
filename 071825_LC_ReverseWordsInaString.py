def reverseWords(s: str) -> str:
    words = s.split()

    words.reverse()
    
    return " ".join(words)

    
if __name__ == '__main__' :
    s = input()
    results = reverseWords(s)
    
    print(results)
    