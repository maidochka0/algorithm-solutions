def get_t():
    def is_plus(v):
        return True if v > 0 else False
    delta_x = (l + x2 - x1) % l
    delta_v = abs(v1 - v2)
    if v1 - v2 < 0:
        delta_x = l - delta_x
    if delta_v == 0:
        if abs(x1) == abs(x2):
            return 0.0
        return None
    return delta_x / delta_v

l, x1, v1, x2, v2 = list(map(int,input().split()))
t = get_t()
x1 = -x1
v1 = -v1
temp = get_t()
if t is None:
    t = temp
elif temp is not None:
    t = min(t, temp)

if t is None:
    print('NO')
else:
    print(f"YES\n{t}")