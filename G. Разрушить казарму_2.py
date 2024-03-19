def get_min_moves():
    def get_overhit_moves():
        def get_kmkz_turn(hp, ally, enemy):

            def get_extra_turn(ally, enemy):
                turn = 0
                while ally > 0 and enemy > 0:
                    enemy -= ally
                    ally -= enemy
                    turn += 1
                if enemy <= 0:
                    return turn
                return -1

            turn = 0
            while hp >= ally and ally > 0:
                turn += 1
                hp -= ally
                ally -= enemy
                enemy += p if hp > 0 else 0

            if ally <= 0:
                return -1
            elif hp > 0:
                turn += 1
                enemy -= ally - hp
                hp = 0
                ally -= enemy
            extra_turn = get_extra_turn(ally, enemy)
            if extra_turn == -1:
                return -1
            return turn + extra_turn


        if x <= p:
            return -1
        ally = x
        enemy = p
        op = x - p
        hp = y - (y - x) // op * op if x < y else y #как посчитать хп?
        turn = 0 if hp == y else (y - x) // op
        kmkz_turn = get_kmkz_turn(hp, ally, enemy)
        total_turn = -1 if kmkz_turn == -1 else turn + kmkz_turn
        while hp > 0:
            kmkz_turn = get_kmkz_turn(hp, ally, enemy)
            if kmkz_turn != -1:
                if total_turn == -1:
                    total_turn = kmkz_turn + turn
                else:
                    total_turn = min(total_turn, kmkz_turn + turn)
            hp -= (x - p)
            turn += 1 # когда увеличивать ходы?
        return total_turn


    def get_kmkz_moves():
        def get_extra_turn(ally, enemy, damage, kmkz_turn):
            turn = 0
            while ally > 0 and enemy > 0:
                turn += 1
                enemy -= ally
                ally -= enemy
            if enemy <= 0 and (x <= p or turn + kmkz_turn < ((damage) + (x - p) - 1) // (x - p)): # взять ближайшее к урону здоровье, полученное безопасной игрой, с округлением вниз
                return turn
            else:
                return None

        damage, total_turn = None, None
        ally = x
        hp = y
        enemy = p
        turn = 0
        while hp >= ally and ally > 0:
            ex_hp = hp
            turn += 1
            hp -= ally
            ex_ally = ally
            ally -= enemy
            ex_enemy = enemy
            if hp > 0:
                enemy += p
            extra_turn = get_extra_turn(ally, enemy, y - hp, turn)
            if extra_turn is not None: # ?
                damage = y - hp
                total_turn = turn + extra_turn
        if ally > 0 and hp > 0:
            turn += 1
            ex_enemy = enemy
            enemy -= ally - hp
            hp = 0
            ex_ally = ally
            ally -= enemy
            extra_turn = get_extra_turn(ally, enemy, y - hp, turn)
            if extra_turn is not None:  # ?
                damage = y - hp
                total_turn = turn + extra_turn
            if enemy <= 0:
                return y, turn
        return damage, total_turn
    damage, total_turn = get_kmkz_moves()
    overhit_turn = get_overhit_moves() # третья
    if damage is None:
        if x <= p:
            ans = -1
        else:
            ans =  (y + (x - p) - 1) // (x - p)
    elif x > p:
        ans = total_turn + (y - damage + (x - p) - 1) // (x - p)
    else:
        ans = total_turn
    if ans == -1:
        ans = overhit_turn
    elif overhit_turn != -1:
        ans = min(overhit_turn, ans)
    return ans
#3 стратегии: сейв, сейв с камикадзе, сейв через оверхит. добавить сейв через оверхит
x = int(input())
y = int(input())
p = int(input())
y -= x
if y <= 0:
    print(1)
else:
    ans = get_min_moves()
    if ans == -1:
        print(ans)
    else:
        print(ans + 1)