lst = int(input())
divider = []

for num in range(1, int(lst ** 0.5) + 1):
    if lst % num == 0:
        divider.append(num)
        divider.append(lst // num)

print(divider)
