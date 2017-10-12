import numpy as np
def knapsack(n, K ):
    W_n = [1, 3, 4, 5]
    Val_n = [1, 4, 5, 7]
    W_knapsack = np.empty([n, K], dtype="int")
    for j in range(0, K):
        W_knapsack[0][j] = 0
    for i in range(1, n):
        for j in range(0, K):
            if (W_n[i] > j):
                W_knapsack[i][j] = W_knapsack[i - 1][j]
            elif ((Val_n[i] + W_knapsack[i - 1][j - W_n[i]] > W_knapsack[i - 1][j])):
                W_knapsack[i][j] = Val_n[i] + W_knapsack[i - 1][j - W_n[i]]
            else:
                W_knapsack[i][j] = W_knapsack[i - 1][j]

    print(list(W_knapsack))
    return W_knapsack


# def main():
#     print(knapsack(4, 9))

# main()

# if __name__ == "__main__":
#     main()
