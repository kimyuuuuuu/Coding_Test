
def compress(chars: list[str]) -> int:
    read = 0
    write = 0
    
    while read < len(chars) :
        current_char = chars[read]
        count = 0 
        
        while read < len(chars) and chars[read] == current_char:
            count += 1 
            read += 1
        
        chars[write] = current_char
        write += 1
        
        if count > 1 :
            count_str = str(count) 
            for digit in count_str :
                chars[write] = digit 
                write += 1
                
            
    return write    

if __name__ == '__main__' :
    chars = list(map(int(input().split(','))))
    
    print(compress(chars))
    
    
# two point 방식