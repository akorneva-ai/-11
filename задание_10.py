lst_1 = list(map(str, input().split()))
lst_2 = list(map(str, input().split()))

range_1, range_2 = map(int, input("Введите диапозон: ").split())
num = lst_1[(range_1 - 1):(range_2 + 1)]

num.reverse()

for _ in num:
    lst_2.append(_)

del lst_1[(range_1 - 1):(range_2 + 1)]

print(lst_1, lst_2)


