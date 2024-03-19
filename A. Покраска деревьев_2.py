
# Считываем данные
P, V = map(int, input().split())
Q, M = map(int, input().split())

# Находим максимальное расстояние, на которое могут отойти Вася и Маша от ведер с краской
max_distance_Vasya = (P + V) if V > 0 else (P - V)
max_distance_Masha = (Q + M) if M > 0 else (Q - M)

# Находим количество деревьев, которые могут быть покрашены
num_trees_painted = abs(Q - P) // 2
if abs(Q - P) % 2 != 0:
    num_trees_painted += 1

# Проверяем, может ли Вася и Маша покрасить все деревья, которые могут быть покрашены
if max_distance_Vasya >= num_trees_painted and max_distance_Masha >= num_trees_painted:
    print(num_trees_painted)
else:
    print(min(max_distance_Vasya, max_distance_Masha))
