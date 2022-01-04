# ATM
# 2021-12-30

N = int(input())

arr = list(map(int, input().split(" ")))
arr2 = []
answer = 0
arr.sort()

for i in arr:
    answer += i
    arr2.append(answer)

print(sum(arr2))
