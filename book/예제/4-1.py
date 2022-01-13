N = int(input())

order = input().split(" ")
x, y = (1, 1)
for i in order:
    if i == "R" and y < 6:
        y += 1
    elif i == "L" and y > 1:
        y -= 1
    elif i == "U" and x > 1:
        x -= 1
    elif i == "D" and x < 6:
        x += 1
    else:
        pass
print(x, y)
