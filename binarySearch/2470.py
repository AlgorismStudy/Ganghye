N = int(input())

arr = list(map(int, input().split()))
arr.sort()

fst = 0
sec = N - 1
max_num = 2000000000

while fst < sec:
    res = arr[fst] + arr[sec]
    if abs(res) < max_num:
        max_num = abs(res)
        answer = [arr[fst], arr[sec]]
    if res < 0:
        fst += 1
    else:
        sec -= 1


print(*sorted(answer), sep=" ")
