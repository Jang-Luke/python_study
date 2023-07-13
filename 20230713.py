#========================
# ◎ 주사위 게임3
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
#  - 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
#  - 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
#  - 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
#  - 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
#  - 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
#========================
a1, b1, c1, d1 = 2, 2, 2, 2
a2, b2, c2, d2 = 4, 1, 4, 4
a3, b3, c3, d3 = 6, 3, 3, 6
a4, b4, c4, d4 = 2, 5, 2, 6
a5, b5, c5, d5 = 6, 4, 2, 5
def solution(a, b, c, d):
    nums = [a, b, c, d]
    value = set()
    duple = {x for x in nums if x in value or (value.add(x) or False)}
    duple = list(duple)
    value = list(value)
    answer = 0
    if len(duple) == 1 and len(value) == 1:
        return 1111 * duple[0]
    elif len(duple) == 1 and len(value) == 2:
        value.remove(duple[0])
        return (10 * duple[0] + value[0])**2
    elif len(duple) == 2 and len(value) == 2:
        return (duple[0] + duple[1]) * abs(duple[0] - duple[1])
    elif len(duple) == 1 and len(value) == 3:
        value.remove(duple[0])
        return value[0] * value[1]
    elif len(duple) == 0 and len(value) == 4:
        return min(value)
print(solution(a1,b1,c1,d1))
print(solution(a2,b2,c2,d2))
print(solution(a3,b3,c3,d3))
print(solution(a4,b4,c4,d4))
print(solution(a5,b5,c5,d5))

#========================
# ◎ 마지막 두 원소
# 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
#========================
num_list1 = [2, 1, 6]
num_list2 = [5, 2, 1, 7, 5]
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    elif num_list[-1] <= num_list[-2]:
        num_list.append(num_list[-1]*2)
    return num_list
print(solution(num_list1))
print(solution(num_list2))

#========================
# ◎ 2016년
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# **제한 조건**
#  - 2016년은 윤년입니다.
#  - 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
#========================
a, b = 5, 24
import datetime as dt
def solution(a, b):
    answer = {0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
    time = dt.datetime(2016, a, b, 0, 0, 0, 0)
    return answer[time.weekday()]
print(solution(a, b))

#========================
# ◎ 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3
#========================
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def isDuple(li, item):
    if len(li) == 0: return False
    if li[-1] == item:
        return True
    else:
        False
def solution(board, moves):
    storage = []
    answer = 0
    stage = {}
    for line in board:
        for index, item in enumerate(line):
            if item == 0:
                continue
            elif stage.get(index) is None:
                stage[index] = [item]
            else:
                stage[index].append(item)
    for num in moves:
        if len(stage[num-1]) == 0: continue
        picked = stage[num-1].pop(0)
        if isDuple(storage, picked):
            storage.pop()
            answer += 2
        else:
            storage.append(picked)
    return answer
print(solution(board, moves))