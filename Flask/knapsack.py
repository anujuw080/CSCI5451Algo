import numpy as np

def knapsack(ln, K ,w):
    W_n = list(map(int,K.split(' ')))
    Val_n = list(map(int,ln.split(' ')))
    n = len(W_n)
    res=knapsackRec(w,W_n,Val_n,n)
    return res 




def knapsackRec(W , wt , val , n):

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapsackRec(W , wt , val , n-1)

    else:
        return max(val[n-1] + knapsackRec(W-wt[n-1] , wt , val , n-1),
                   knapsackRec(W , wt , val , n-1))
