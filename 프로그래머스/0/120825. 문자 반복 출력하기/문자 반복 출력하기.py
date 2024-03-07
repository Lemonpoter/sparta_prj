def solution(my_string, n):
    
    answer = []
    
    for str in my_string:
        answer.append(str*n)
    return "".join(answer)