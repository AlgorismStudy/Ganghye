def solution():
    N = int(input())
    answer = 0

    while N >= 0:
        sugar_5 = N // 5
        if N % 5 == 0:
            answer += sugar_5
            break
        N -= 3
        answer += 1
    else:
        answer = -1
    return answer


if __name__ == "__main__":
    solution()
