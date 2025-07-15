def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    i = 0 
    print(len(flowerbed))
    
    while i < (len(flowerbed))  :
        print("i: ", i)
        print("n: ", n)
        if flowerbed[i] == 1 : 
            i = i+2 
            
        else :
            if (i+1 >= len(flowerbed)) or (flowerbed[i+1] == 0):
                n = n - 1 
                i = i + 2 
            else :
                i = i + 2 
                
    print("result n : ", n)
    if n == 0 :
        return True
    
    else : 
        return False
    
if __name__ == '__main__' : 
    flowerbed = list(map(int, input().split(',')))
    n = int(input())
    
    results = canPlaceFlowers(flowerbed, n)
    print(results)
    
# 1. [1,0,0,0,1,0,0], n=2 처럼 심을 수 있는 공간이 맨 마지막에 있는 경우를 고려하지 않았음 
#    => while문의 조건을 len(flowerbed)로 변경하여 끝까지 돌되, (i+1 >= len(flowerbed))를 추가하여 맨 끝인지 아닌지 확인하고자 함
# 2. 우려하던 list index out of range 발생
#    => 첫 번째 if문에서 발생 