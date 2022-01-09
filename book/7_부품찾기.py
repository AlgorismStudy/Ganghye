N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))


def binary(list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


N_list.sort()
for i in M_list:
    res = binary(N_list, i, 0, N - 1)
    if res != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
