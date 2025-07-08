def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    results = [] 
    max_candy = max(candies)
    
    for i in range(len(candies)) :
        if candies[i] + extraCandies >= max_candy :
            results.append(True)
            
        else :
            results.append(False)
    return results
    
    
if __name__ == '__main__' :
    candies = list(map(int, input().split(',')))
    extraCandies = int(input())
    
    print(candies, extraCandies)
    
    results = kidsWithCandies(candies, extraCandies) 
    print(results)
    