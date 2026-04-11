lst = list(map(int, input().split()))

even_num = 0
odd_num = 0


for num in lst:
    if num % 2 == 0:
        even_num += num
    elif num % 2 != 0:
        odd_num += num

print(even_num, odd_num)