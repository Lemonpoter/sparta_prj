def solution(n):
    for num in range(1, n+1):
        if num ** 2 == n:
            return 1
    return 2