def pivotIndex(nums: list[int]) -> int:
    prefix = [0] * (len(gain)+1)
    
    for i in range(1, len(gain)+1) :
        prefix[i] = gain[i-1] + prefix[i-1]
        
    return max(prefix)
    
    
if __name__ == '__main__':
    gain = list(map(int, input.split(',')))
    
    print(pivotIndex(gain))
    