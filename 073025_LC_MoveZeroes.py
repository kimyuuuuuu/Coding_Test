def moveZeroes(nums: list[int]) -> None:
    write = 0
    
    for i in range(len(nums)) :
        if nums[i] != 0 :
            nums[write] = nums[i]
            write += 1
            
    while write < len(nums) :
        nums[write] = 0
        write += 1            
        
    
if __name__ == '__main__' :
    chars = list(map(int(input().split(','))))
    
    print(moveZeroes(chars))
    
    