def solution(array, n):
    array.sort()
    answer = array[0]
    x = abs(n - array[0])
    for i in array:
        if x > abs(n - i):
            x = abs(n - i)
            answer = i
    return answer
