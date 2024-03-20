def solution(cipher, code):
    answer = ''
    for c in range(len(cipher)):
        if (c+1) % code == 0:
            answer += cipher[c]
    return answer