def calculate_clicks(n):
    num_clicks = n // 4
    n = n % 4
    match n:
        case 1:
            num_clicks += 1
        case 2 | 3:
            num_clicks += 2
    return num_clicks
ans = 0
for i in range(int(input())):
    ans += calculate_clicks(int(input()))
print(ans)