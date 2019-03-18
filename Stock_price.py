
""" 
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 4 and sell on day 6. 
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
Author: Kaveh Ahmadi
"""

class solution:
    def __init__(self,List):
        self.L = List
    def max_profit(self):
        max_p = 0
        best_buy_i_temp = 0
        best_sell_i = -1
        best_buy_i = -1

        for i in range(1,len(self.L)):
            if self.L[i]<self.L[best_buy_i_temp]:
                best_buy_i_temp = i
            elif max_p < (self.L[i]-self.L[best_buy_i_temp]):
                max_p = self.L[i]-self.L[best_buy_i_temp]
                best_sell_i = i
                best_buy_i = best_buy_i_temp

        return(max_p, best_buy_i, best_sell_i)
        
if __name__ == "__main__":
    
    L = [6,2,3,1,4,5,37,4,1,8,2]
    S = solution(L)

    max_profit, best_buy_i, best_sell_i = S.max_profit()
    if max_profit>0:
        print("Maximum profit could be:", max_profit , " Buy at:",L[best_buy_i], " Sell at:",L[best_sell_i])
    else:
        print('There is no profit in this trade')


    


