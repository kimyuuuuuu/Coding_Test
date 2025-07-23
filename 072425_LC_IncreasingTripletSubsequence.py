def increasingTriplet(nums: list[int]) -> bool:
    result = 1
    result_idx = 0
    current_num = nums[0]
    
    for i, num in enumerate(nums) :
        if current_num >= num :
            result = 1
            result_idx = i
            
        elif current_num < num and result_idx < i : 
            result += 1
            
        if result == 3 :
            return True 
            
        current_num = num 
        
        print(num, ':', result, current_num, result_idx)
            
    return False
            
    
if __name__ == '__main__' :
    s = list(map(int, input().split(',')))
    
    print(increasingTriplet(s))
    
# 1. 문제 이해 실수 .. 연속되지 않아도 됨 (index가 작기만 하면 됨, i < j < k)