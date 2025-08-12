def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    result = 0
    
    while left < right :
        current_sum = nums[right] + nums[left]
        # print("current_sum: ", current_sum)
        # print("left: ", left, "right: ", right)
        if current_sum == k :
            result += 1
            left += 1
            right -= 1
            # print("result: ", result)
            
        elif current_sum < k :
            left += 1
            
        else :
            right -= 1
            
    return result
    
if __name__ == '__main__' :
    nums = list(map(int, input().split(',')))
    k = int(input())

    print(maxOperations(nums, k))