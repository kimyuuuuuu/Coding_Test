def largestAltitude(gain: list[int]) -> int:
    prefix = [0] * (len(gain)+1)
    
    for i in range(1, len(gain)+1) :
        prefix[i] = gain[i-1] + prefix[i-1]
        
    return max(prefix)
    
    
if __name__ == '__main__':
    gain = list(map(int, input.split(',')))
    
    print(largestAltitude(gain))
    
# prefix sum시 prefix의 이전 값과 합산 => for문을 1부터 시작 
# => prefix가 미리 존재해야 1부터 시작 가능 & 이전 값 합산 가능 (prefix = [0] * (len(gain)+1))