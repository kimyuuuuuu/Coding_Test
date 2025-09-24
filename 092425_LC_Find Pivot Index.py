def pivotIndex(nums: list[int]) -> int:
    prefix = [0] * (len(nums)+1)
    prefix_len = len(prefix)
    
    # create prefix sum 
    for i in range(1, len(nums)+1):
        prefix[i] = nums[i-1] + prefix[i-1]
        
        
    for j in range(len(nums)) :
        if prefix[0] == prefix[prefix_len-j] :
            return j 
    
    return -1
    
if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    
    print(pivotIndex(nums))
    