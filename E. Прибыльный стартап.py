def find_profit(n, k, d):
    for i in range(1, d+1):
        for j in range(10):
            profit = n * 10 + j
            if profit % k == 0:
                profit = str(profit) + '0' * (d - i)
                return profit 
        return -1 

while True:
    n, k, d = map(int, input().split())
    result = find_profit(n, k, d)
    print(result)
