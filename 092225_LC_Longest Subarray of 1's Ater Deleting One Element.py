def longestSubarray(self, nums: list[int]) -> int:
    left, zeros, answer = 0, 0, 0
    
    if 1 not in nums :
        return 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        
        while zeros > 1 :
            if nums[left] == 0:
                zeros -= 1
            left += 1
            
        answer = max(answer, right - left)
                
    return answer


if __name__ == '__main__' :
    nums = list(map(int, input().split(',')))
    print(longestSubarray(nums))
    
# 슬라이딩 윈도우
# 왼쪽 고정, 오른쪽을 옮겨가며 0이 1개 초과해서 나올때까지 윈도우 크기 증가
# 0이 초과할 경우 왼쪽을 옮겨가며 0이 있는 위치까지 윈도우 줄이기