def productExceptSelf(nums: list[int]) -> list[int] :
    result = [] 
    zero = False
    j = nums[0]
    
    for i in range(len(nums)-1) :
        if nums[i+1] == 0 :
            zero = True
            continue 
        j = nums[i+1]*j
    
        
    if zero : 
        for i in nums :
            if i != 0 :
                result.append(0)
            else :
                result.append(j)
                
    else :
        for i in nums : 
            result.append(int(j/i))
        
    return result

if __name__ == '__main__' :
    s = list(map(int, input().split(',')))
    
    results = productExceptSelf(s)
    print(results)

# 1. [0,0]의 case를 생각 못 함 -> j = nums[0]으로 둠
# 2. 여러 수가 들어간 리스트에서 0이 여러 개인 경우 생각 못함 
