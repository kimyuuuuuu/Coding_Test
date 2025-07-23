def productExceptSelf(nums: list[int]) -> list[int] :
    result = [] 
    zero = 0
    j = 1
    
    for i in range(len(nums)) :
        if nums[i] == 0 :
            zero += 1
            continue 
        j = nums[i]*j
    
    if zero == 1: 
        for i in nums :
            if i != 0 :
                result.append(0)
            else :
                result.append(j)
    
    elif zero >= 1 :
        result.extend([0] * len(nums))
                
    else :
        for i in nums : 
            result.append(int(j/i))
        
    return result

if __name__ == '__main__' :
    s = list(map(int, input().split(',')))
    
    results = productExceptSelf(s)
    print(results)

# 1. [0,0]의 case를 생각 못 함 -> j = nums[0]으로 둠
# 2. 여러 수가 들어간 리스트에서 0이 여러 개인 경우 생각 못함 -> 0의 갯수에 따라 다른 과정
# +) 처음 풀었을 때 보다 Runtime이 240ms 줄음...