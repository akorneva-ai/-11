lst = list(map(int, input().split()))

for num in lst:
    num = sum(lst) / len(lst)

print(num)