n = int(input("Введите кол-во чисел N "))
sum = 0
for i in range(1, n + 1):
    x = int(input("Введите числа, до кол-ва N - "))
    if x == 0: sum += 1

print(sum)