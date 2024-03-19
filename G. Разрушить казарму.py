def min_moves(x, y, p):
    '''
    if x > p:
        if x >= y:
            return 1
        ans = 1
        y -= x
        overhit = x - p
        ans += (y + overhit - 1) // overhit
        return ans
    '''
    army = 0
    move_num = 0
    while x < y and x > 0:
        move_num += 1
        y -= x
        x -= army
        army += p
    if y > 0:
        move_num += 1
        overhit = x - y
        army -= overhit
        x -= army
    while x > 0 and army > 0:
        move_num += 1
        army -= x
        x -= army
    if army <= 0:
        return move_num
    else:
        return -1
while True:
    x = int(input())
    y = int(input())
    p = int(input())
    anss = []
    ans_2 = (min_moves(x, y, p))
    if ans_2 != -1:
        anss.append(ans_2)
    if x > p:
        y -= x
        ans = 1
        x -= p
        p = 0
        ans_1 = min_moves(x, y, p) + ans
        if ans_1 != -1:
            anss.append(ans_1)
    if len(anss) == 0:
        anss = [-1]
    print(min(anss))