def increasingTriplet(nums: list[int]) -> bool:
    result = 1
    current_num = nums[0]
    
    for i, num in enumerate(nums) :
        if current_num >= num :
            result = 1
            
        else : 
            result += 1
            
        if result == 3 :
            return True 
        
        print(result, current_num, num)
            
        current_num = num 
        
            
    return False
            
    
if __name__ == '__main__' :
    s = list(map(int, input().split(',')))
    
    print(increasingTriplet(s))
    
# 1. 문제 이해 실수 .. 연속되지 않아도 됨 (index가 작기만 하면 됨, i < j < k)