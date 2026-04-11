number = input().split()

number = [int(num) for num in number]

result = []

for _ in number:
    if _ != 3:
        result.append(_)

print(result)