class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed.insert(0,0)
        flowerbed.append(0)

        counter = 0

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter = counter + 1
    
        return counter >= n