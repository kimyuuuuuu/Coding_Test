def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n== 0 :
        return True 
    
    for i in range(len(flowerbed)) : 
        if flowerbed[i] == 0 :
            left_check = (i==0) or (flowerbed[i-1]==0)
            right_check = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
            if left_check and right_check :
                flowerbed[i] = 1 
                n -= 1 
                if n == 0 :
                    return True 
                
    return False
    
    
    
if __name__ == '__main__' : 
    flowerbed = list(map(int, input().split(',')))
    n = int(input())
    
    results = canPlaceFlowers(flowerbed, n)
    print(results)
    
# 1. [1,0,0,0,1,0,0], n=2 처럼 심을 수 있는 공간이 맨 마지막에 있는 경우를 고려하지 않았음 
#    => while문의 조건을 len(flowerbed)로 변경하여 끝까지 돌되, (i+1 >= len(flowerbed))를 추가하여 맨 끝인지 아닌지 확인하고자 함
# 2. 우려하던 list index out of range 발생
#    => 첫 번째 if문에서 발생, while 문의 조건을 <= 에서 <으로 변경
# 3. [0,1,0] 과 같은 상황에서, 마지막이 0일 때 왼쪽을 체크하지 않아 문제 발생
#    => (flowerbed[i-1] == 0) 를 추가하여 왼쪽 확인 
# 4. [0,0,1,0,0] n=1 에서 심을 수 있는 곳이 2군데 있어서 n이 -1이 됨 .. 
#    => n이 0이 보다 작으면 return true
# 5. [0,1,0,1,0,1,0,0]에서 n=1일 때 ... flowerbed가 짝수인 것만 생각하고 코드를 짬.. 홀수도 고려했어야 함
#    => 코드 전면 수정 ..... 
# 6. n=0인 경우 확인 .......해야함.......