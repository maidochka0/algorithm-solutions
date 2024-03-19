def count_trees(p, v, q, m):
        if p > q:
            p, v, q, m = q, m, p, v
        ans = (v + m + 1) * 2 - max(0, (min( q + m, p + v) - max(p - v, q - m) + 1))
        if v == 0 or m == 0:
            ans = (v + m) * 2 + 1
        if v == 0 and m == 0:
            ans = 0
        
        return ans
p, v = map(int, input().split())
q, m = map(int, input().split())
print(count_trees(p, v, q, m))
