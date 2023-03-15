
x, y = map(int, input('Ввидите 2-а числа ').split())
z = 0
for i in range(x + y):
    if z:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            z = 1
            print(*sorted([i, j]))

            









