arr = [1,2,3,1,2]
n = 3
# 1 3 6 7 9
def solution(arr, n):
    answer = 0
    length = len(arr)
    s = [0] * length
    c = [0] * n
    s[0] = arr[0]
    for i in range(1, length):
        s[i] = s[i-1] + arr[i]
    for i in range(length):
        remain = s[i] % n
        if remain == 0:
            answer += 1
        c[remain] += 1
    for i in range(n):
        answer += (c[i] * (c[i] - 1)) // 2
    return answer
print(solution(arr, n))