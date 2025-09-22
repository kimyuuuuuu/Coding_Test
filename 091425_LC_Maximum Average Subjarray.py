# def findMaxAverage(nums: list[int], k: int) -> float:
#   array = []

#   for i in range(len(nums)-k+1):
#     array.append(sum(nums[i:i+k])/k)

#   return max(array)


# if __name__ == '__main__' :
#   nums = list(map(int, input().split(',')))
#   k = int(input())

#   print(nums, k)

#   print(findMaxAverage(nums, k))

# error
# 1. for i in range(len(nums)-k+1): #k를 다 빼면 덜 돈다 ..
# 2. Time limit error : 시간이 부족함
#    => 1) 슬라이딩 윈도우로 매번 새로 계산하지 않고 앞빼고뒤더하는방식사용
#    => 2) max를 array에 저장 X 최대면 업데이트하는 방식 사용

def findMaxAverage(nums: list[int], k: int) -> float:
  max_average = float('-inf')
  average = sum(nums[0:k]/k)

  for i in range(1, len(nums)-k+1):
    average = average - nums[i] + nums[i+4]
    if max_average < average / k:
      max_average = average / k

  return max_average


if __name__ == '__main__' :
  nums = list(map(int, input().split(',')))
  k = int(input())

  print(nums, k)

  print(findMaxAverage(nums, k))