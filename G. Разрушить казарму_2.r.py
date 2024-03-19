def count_extra_moves(ally, enemy):
    turn = 0
    while ally > 0 and enemy > 0:
        turn += 1
        enemy -= ally
        ally -= enemy
    if enemy <= 0:
        return turn
    return None
def count_overhit_moves():
    if x <= p and x < y:
        return None
    elif x <= p and x >= y:
        op = y
    else:
        op = x - p
    total_turn = None
    if y > x:
        hp = y - (y - x) // op * op
        turn = (y - x) // op
    else:
        hp = y
        turn = 0
    while hp > 0:
        turn += 1
        OH_enemy = p - (x - hp)
        OH_ally = x - OH_enemy
        extra_moves = count_extra_moves(OH_ally, OH_enemy)
        if extra_moves is not None:
            if total_turn is None:
                total_turn = extra_moves + turn
            else:
                total_turn = min(total_turn, extra_moves + turn)
        hp -= op
    return total_turn
def count_kmkz_moves():
    hp = y
    ally = x
    enemy = p
    turn = 0
    total_turn = None
    total_kmkz_turn = None
    damage = 0
    while ally > 0 and hp > 0:
        turn += 1
        enemy -= max(0, ally - hp)
        hp -= ally
        ally -= enemy
        enemy += p if hp > 0 else 0
        extra_moves = count_extra_moves(ally, enemy)
        if extra_moves is not None:
            damage = y - hp
            total_kmkz_turn = turn + extra_moves
    if x <= p:
        return total_kmkz_turn if damage >= y else None
    else:
        if total_kmkz_turn is None:
            return None
        op = x - p
        return total_kmkz_turn + max(0, (y - damage + op - 1) // op)

x = int(input())
y = int(input())
p = int(input())
y -= x
ans = []
temp = count_kmkz_moves()
if temp is not None:
    ans.append(temp)
temp = count_overhit_moves()
if temp is not None:
    ans.append(temp)
print(ans)
if y <= 0:
    print(1)
else:
    print(-1 if len(ans) == 0 else min(ans) + 1)