#Подбрасываем монетку 100 раз и смотрим что выйдет
import random
count = 0
orel = 0
reshka = 0
while count != 100:
    podbros = random.randint (1,2)
    if podbros == 1:
        orel += 1
    else:
        reshka += 1
    count += 1
print('Орел ', orel, 'Решка ', reshka)

