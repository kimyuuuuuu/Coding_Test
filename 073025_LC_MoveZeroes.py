def moveZeroes(nums: list[int]) -> None:
    count = 0
    for i in range(len(nums)) :
        if nums[i] == 0 :
            count += 1 
            del nums[i]
            
    nums.extend([0] * count)
    

if __name__ == '__main__' :
    chars = list(map(int(input().split(','))))
    
    print(moveZeroes(chars))
    
    