def longestOnes(self, nums: list[int], k: int) -> int:
  left, zeros, max_length = 0

  for right in range(len(nums)):
    if nums[right] == 0 :
      zeros += 1

    while zeros > k :
      if nums[left] == 0:
        zeros -= 1
      left += 1

    max_length = max(max_length, right - left + 1)
  return max_length

if __name__ == '__main__' :
  nums = list(map(int, input().split(',')))
  k = int(input())

  print(nums, k)

  print(longestOnes(nums, k))

  # error
  # 1. 연속성을 고려하지 않음
  #    => Two pointer로 윈도우를 관리하면서 0이 K개 이상 나오면 왼쪽 포인터를 줄여나감