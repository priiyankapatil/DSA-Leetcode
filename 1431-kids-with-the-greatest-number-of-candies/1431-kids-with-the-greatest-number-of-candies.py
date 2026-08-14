class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        total=[i+extraCandies for i in candies]
        maximum=max(candies)
        for i in total:
            if i>=maximum:
                res.append(True)
            else:
                res.append(False)
        
        return res