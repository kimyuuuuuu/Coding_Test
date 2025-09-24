def pivotIndex(nums: list[int]) -> int:
    prefix = [0] * (len(nums)+1)
    prefix_len = len(prefix) -1
    
    # create prefix sum 
    for i in range(1, len(nums)+1):
        prefix[i] = nums[i-1] + prefix[i-1]
        
        
    for j in range(len(nums)) :
        if prefix[j] == (prefix[prefix_len] - prefix[j+1]) :
            return j 
    
    return -1
    
if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    
    print(pivotIndex(nums))
    
# len(prefix) 하면 길이는 7인데 마지막 인덱스는 6인 경우들 발생 => out of range
# 바보같이 빼기 안하고 인덱스 빼기 함 .... prefix[prefix_len-j]