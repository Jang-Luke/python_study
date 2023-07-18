#========================
# 두 수의 연산값 비교하기
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
#  - 12 ⊕ 3 = 123
#  - 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
#========================
a = 2
b = 91
print(int(str(a)+str(b)))
def solution(a, b):
    return max(int(str(a)+str(b)), (2*a*b))
print(solution(a,b))

#========================
# 이상한 문자 만들기
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
#  - 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
#  - 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
#========================
s = "try hello world "
result = "TrY HeLlO WoRlD"
print(s.endswith(" "))
def solution(s):
    answer = []
    splitStr = s.split(" ")
    for index, str in enumerate(splitStr):
        if index != 0:
            answer.append(" ")
        for idx, alphabet in enumerate(str):
            if idx % 2 == 0:
                answer.append(alphabet.upper())
            else:
                answer.append(alphabet.lower())
    return "".join(answer)
print(solution(s))

#========================
# # 서울에서 김서방 찾기
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
# "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
#========================
seoul = ["Jane", "Kim"]
print(seoul.index("Kim"))
result = "김서방은 1에 있다"
def solution(seoul):
    return "김서방은 {0}에 있다".format(seoul.index("Kim"))

#========================
# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3
#========================
lottos1 = [44,1,0,0,31,25]
win_nums1 = [31,10,45,1,6,19]
result1 = [3,5]
lottos2 = [0,0,0,0,0,0]
win_nums2 = [38,19,20,40,15,25]
result2 = [1,6]
lottos3 = [45,4,35,20,3,9]
win_nums3 = [20,9,3,45,4,35]
result3 = [1,1]

def solution(lottos, win_nums):
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    unknown = lottos.count(0)
    count = len([wnum for num in win_nums for wnum in lottos if num == wnum])
    return [rank[count+unknown], rank[count]]
print(solution(lottos1, win_nums1))
print(solution(lottos2, win_nums2))
print(solution(lottos3, win_nums3))

#========================
# K번째 수
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
#  - array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#  - 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#  - 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#========================
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
def solution(array, commands):
    answer = []
    for index, value in enumerate(commands):
        answer.append(sorted(array[value[0]-1:value[1]]).pop(value[2]-1))
    return answer
print(solution(array, commands))

#========================
# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
#========================
s1 = "one4seveneight"
s2 = "23four5six7"
s3 = "2three45sixseven"
s4 = "123"
def solution(s):
    code = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for key, value in code.items():
        s = s.replace(key, str(value))
    return int(s)
print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
dic = {1:"A", 2:"B", 3:"C"}
print(dic.items())
listt = [1,2,3,4,5]
print(enumerate(listt))