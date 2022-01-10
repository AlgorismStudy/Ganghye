# 이진탐색

n, x = map(int, input().split())

arr = list(map(int, input().split()))
start = 0
end = len(arr)


def first(arr, start, end, target):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            answer = min(mid, answer)
        elif target < arr[mid]:
            end = mid
        else:
            start = mid + 1
    return answer


def last(arr, start, end, target):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            answer = max(mid, answer)
        elif target < arr[mid]:
            end = mid
        else:
            start = mid + 1
    return answer


print(first(arr, start, end, x))
# print(last(arr, start, end, x))
