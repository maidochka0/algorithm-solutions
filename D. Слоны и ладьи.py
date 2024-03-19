def rook_funct(x, y):
    x_offsets = [0, +1, 0, -1]
    y_offsets = [-1, 0, +1, 0]
    for i in range(4):
        x_temp = x + x_offsets[i]
        y_temp = y + y_offsets[i]
        while desk[y_temp][x_temp] not in stop_flags:
            desk[y_temp][x_temp] = '+'
            x_temp += x_offsets[i]
            y_temp += y_offsets[i]
def bishop_funct(x, y):
    x_offsets = [+1, +1, -1, -1]
    y_offsets = [-1, +1, +1, -1]
    for i in range(4):
        x_temp = x + x_offsets[i]
        y_temp = y + y_offsets[i]
        while desk[y_temp][x_temp] not in stop_flags:
            desk[y_temp][x_temp] = '+'
            x_temp += x_offsets[i]
            y_temp += y_offsets[i]        
desk = [[None] * 10]
for i in range(8):
    line = []
    line.append(None)
    line.extend(list(input().strip()))
    line.append(None)
    desk.append(line)
desk.append([None] * 10)

stop_flags = ['R', 'B', None]

for i in range(1,9):
    for j in range(1, 9):
        if desk[i][j] == 'R':
            rook_funct(j, i)
        elif desk[i][j] == 'B':
            bishop_funct(j, i)
        else:
            continue
ans = 0
for i in range(1, 9):
    ans += desk[i].count('*')
print(ans)