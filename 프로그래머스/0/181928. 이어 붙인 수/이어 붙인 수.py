def solution(num_list):
    odd = ''
    even = ''
    for n in num_list:
        if n % 2 == 1:
            odd += str(n)
        elif n % 2 == 0:
            even += str(n)
    return int(odd) + int(even)