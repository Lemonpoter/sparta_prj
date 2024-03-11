def solution(num_list):
    answer = 1
    answer2= 0
    for num in num_list:
        answer *= num
        answer2 = answer2 + num
    answer2 = answer2**2
    
    if answer2 > answer:
        return 1
    else:
        return 0