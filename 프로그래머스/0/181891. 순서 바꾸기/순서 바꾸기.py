def solution(num_list, n):
    result = num_list[n:] + num_list[:n]
    return result