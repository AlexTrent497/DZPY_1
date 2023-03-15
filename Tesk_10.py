
n = int(input('колличиство монет  '))
eagle = tails = 0
for _ in range(n):
    a = int(input('орёл(1) или решка(0)'))
    if a == 1:
        eagle += 1
    else:
        tails += 1
if eagle < tails:
    print(f'переверните {eagle} монет с орла на решку, их меньше всего')
elif eagle == tails:
    print(f'колличество орлов и решек равно, по {eagle} штук')
else:
    print(f'переверните {tails} монет с решки на орла, их меньше всего')




