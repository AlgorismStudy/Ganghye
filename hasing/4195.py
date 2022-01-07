N = int(input())


for _ in range(N):
    M = int(input())
    s = set()
    d = dict()
    for _ in range(M):

        per1, per2 = input().split()
        if per1 in s or per2 in s:
            d[per1] += 1
            d[per1] += 1
        if per2 in s:
            d[per2] += 1

        if per1 not in s:
            d[per1] = 1
            s.add(per1)
        if per2 not in s:
            d[per2] = 1
            s.add(per2)
        print(d)
        print(s)
