def solution(num_list):
    even = 0
    odd = 0
    for num in range(len(num_list)):
        if num % 2 == 0:
            even += num_list[num]
        elif num % 2 == 1:
            odd += num_list[num]

    if even > odd:
        return even
    elif odd > even:
        return odd
    else:
        return even
