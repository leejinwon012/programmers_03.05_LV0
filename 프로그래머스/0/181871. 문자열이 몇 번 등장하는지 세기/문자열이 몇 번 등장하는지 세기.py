def solution(myString, pat):
    answer = 0

    for i in range(len(myString) + 1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer