# 회의실 배정

n_list = []
t_list = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split(" "))
    if len(n_list) == 0:  # 첫 원소는 그냥 push
        n_list.append((a, b))
        t_list.append(b - a)
    else:
        if (
            n_list[-1][-1] > a and b - a < t_list[-1]
        ):  # 기존원소의 종료시간 > 새로운원소의 종료시간 && 새로운원소의 기존원소의 진행시간보다 짧으면 기존원소 빼고 새로운원소 넣기
            n_list.pop()
            t_list.pop()
            n_list.append((a, b))
            t_list.append(b - a)
        elif (
            n_list[-1][-1] <= a and b - a < t_list[-1]
        ):  # 새로운원소 시작시간이 기존원소의 종료시간과 같거나 늦으면 새로운원소 넣기
            n_list.append((a, b))
            t_list.append(b - a)


print(len(t_list))
