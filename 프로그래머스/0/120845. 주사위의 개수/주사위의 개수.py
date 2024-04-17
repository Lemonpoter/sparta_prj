def solution(box, n):
    answer = [x//n for x in box]
    return answer[0] * answer[1] * answer[2]