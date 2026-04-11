number = input().split()

number = [int(num) for num in number]

result = []

for _ in range(8):
    result.append(number[_] + number[_ + 1])

print(result)

