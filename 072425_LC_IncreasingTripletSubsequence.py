def increasingTriplet(nums: list[int]) -> bool:
    small, mid = float('inf'), float('inf')
    
    for i in nums:
        if i <= small :
            small = i
        elif i <= mid :
            mid = i 
        else :
            return True
            
    return False
            
    
if __name__ == '__main__' :
    s = list(map(int, input().split(',')))
    
    print(increasingTriplet(s))
    
# 1. 문제 이해 실수 .. 연속되지 않아도 됨 (index가 작기만 하면 됨, i < j < k)
# 2. 이해 못함 다시 볼것.