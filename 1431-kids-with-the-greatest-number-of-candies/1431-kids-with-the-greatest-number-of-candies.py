class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maximum = max(candies)

        for i in candies:
            if i + extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)
        
        return res