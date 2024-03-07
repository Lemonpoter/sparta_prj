def solution(n):
    answer = []
    for num in range(1,n+1):
        if n % num == 0:
            answer.extend([num, n // num])
    return len(answer) // 2