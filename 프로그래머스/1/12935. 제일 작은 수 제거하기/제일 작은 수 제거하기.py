def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        answer = min(arr)
        arr.remove(answer)
        return arr