def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    i = 0 
    
    while i < (len(flowerbed) - 2)  :
        print("i: ", i)
        print("n: ", n)
        if flowerbed[i] == 1 : 
            i = i+2 
            
        else :
            if flowerbed[i+1] == 0 :
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