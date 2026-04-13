lst = input().split()
command = input()

direction = command[0]
k = int(command[1:])

if direction == "R":
    result = lst[-k:] + lst[:-k]

elif direction == "L":
    result = lst[k:] + lst[:k]

print(result)