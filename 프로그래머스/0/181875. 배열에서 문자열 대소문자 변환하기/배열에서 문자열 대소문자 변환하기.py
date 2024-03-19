def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if strArr[i % 2] == strArr[1]:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer