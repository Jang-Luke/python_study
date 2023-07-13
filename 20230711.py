#========================
# ◎ 배열 조각하기
# 정수 배열 arr와 query가 주어집니다.

# query를 순회하면서 다음 작업을 반복합니다.

# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
# 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 입출력 예
# arr	query	result
# [0, 1, 2, 3, 4, 5]	[4, 1, 2]	[1, 2, 3]
#========================
arr = [0,1,2,3,4,5]
query = [4,1,2]
def solution(arr, query):
    for i in range(0,len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr
print(solution(arr, query))

#========================
# ◎ A 강조하기
# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
#========================
myString1 = 'abstract algebra'
myString2 = 'PrOgRaMmErS'
def solution(myString):
    myString = myString.lower().replace('a', 'A')
    return myString
print(solution(myString1))
print(solution(myString2))
#========================
# ◎ 정수 부분
# 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.
#========================
import math
flo1 = 1.42
flo2 = 69.32
def solution(flo):
    return math.floor(flo)
print(solution(flo1))
print(solution(flo2))
#========================
# ◎ 제일 작은 수 제거하기
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
#========================
arr1 = [4,3,2,1,1,1]
arr2 = [10]
def solution(arr):
    min = 0
    for index, value in enumerate(arr):
        if index == 0:
            min = value
        min = value if value < min else min
    arr.remove(min)
    return [-1] if len(arr) == 0 else arr
print(solution(arr1))
print(solution(arr2))