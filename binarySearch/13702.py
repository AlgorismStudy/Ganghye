n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
start = 0
end = max(arr)
person = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in arr:
        temp += i // mid
    # print('mid:', mid, 'person:', temp)
    if temp < k:  # 사람수가 k보다 적으면 -> 술을 너무 많이 줘서 못받는 인원 있음
        end = mid - 1
    elif temp >= k:  # 사람수가 k보다 많으면 -> 모든 인원이 술을 받을 수 있지만 더 큰 용량으로 줄 수 있는지 찾아볼 필요 있음
        person = temp
        start = mid + 1

print(end)
