def solution(arr,n):
    answer = []
    for a in range(len(arr)):
        if len(arr) % 2 == 1:
            if a % 2 == 0:
                answer.append(arr[a]+n)
            else:
                answer.append(arr[a])
        elif len(arr) % 2 == 0:
            if a % 2 == 1:
                answer.append(arr[a]+n)
            else:
                answer.append(arr[a])
    return answer
