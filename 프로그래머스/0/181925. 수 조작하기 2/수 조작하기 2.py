def solution(numlog):
    answer = ''
    dic = {1:'w',-1:'s', 10:'d', -10:'a'}

    for idx, val in enumerate(numlog):
        if idx != len(numlog)-1:
            answer += dic[numlog[idx +1] - numlog[idx]]

    return answer