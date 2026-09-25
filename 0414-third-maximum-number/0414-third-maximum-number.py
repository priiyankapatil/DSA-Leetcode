class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        largest=float('-inf')
        second=float('-inf')
        third=float('-inf')

        for x in nums:
            if x==largest or x==second or x==third:
                continue
            if x>largest:
                third=second
                second=largest
                largest=x
            elif x>second and x!=largest:
                third=second
                second=x
            elif x>third and x!=second:
                third=x
        
        if third == float('-inf'):
            return largest

        return third
