class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # buy=prices[0]

        # for i in range(1,len(prices)):
        #     sell=prices[i]
        #     profit=sell-buy
        #     if profit<0:
        #         buy=prices[i]
        #     if profit>max_profit:
        #         max_profit=profit

        # return max_profit

        min_price=prices[0]
        profit=0

        for i in range(1,len(prices)):
            curr_profit=prices[i]-min_price
            if curr_profit>profit:
                profit=curr_profit
            min_price=min(min_price,prices[i])

        return profit