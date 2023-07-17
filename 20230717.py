#========================
# 나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
#========================
arr = [5, 9, 7, 10]
divisor = 5
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer
print(solution(arr,divisor))
#========================
# 햄버거 만들기
# 햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다.
# 함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고,
# 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다.
# 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다.
# 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며,
# 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.
# 예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때,
# 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다.
# 즉, 2개의 햄버거를 포장하게 됩니다.
# 상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

# 1 ≤ ingredient의 길이 ≤ 1,000,000
# ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.
#========================
ingredient1 = [2,1,1,2,3,1,2,3,1] #2
ingredient2 = [1,3,2,1,2,1,3,1,2] #0
def solution(ingredient):
    return makeOne(ingredient, 0)
def makeOne(ingredient, answer):
    count = answer
    length = len(ingredient)
    for index, value in enumerate(ingredient):
        if (index+4) > length: break
        if (
            ingredient[index] == 1 and
            ingredient[index+1] == 2 and
            ingredient[index+2] == 3 and
            ingredient[index+3] == 1
        ):
            count += 1
            for i in range(0,4):
                ingredient.pop(index)
            count = makeOne(ingredient, count)
            break
    return count
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        length = len(stack)
        if stack[length-4:] == [1,2,3,1]:
            answer += 1
            for j in range(0,4):
                stack.pop()
    return answer
print(ingredient1[2:6]==[1,2,3,1])
print(solution(ingredient1))

#========================
# 수열과 구간 쿼리 3
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
#========================
arr = [0,1,2,3,4]
queries = [[0,3], [1,2], [1,4]]
def solution(arr, queries):
    for index, value in enumerate(queries):
        print(value)
        tmp = arr[value[0]]
        arr[value[0]] = arr[value[1]]
        arr[value[1]] = tmp
    return arr
print(solution(arr, queries))

#========================
# 과일 장수
# 과일 장수가 사과 상자를 포장하고 있습니다.
# 사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 사과 한 상자의 가격은 다음과 같이 결정됩니다.
#  - 한 상자에 사과를 m개씩 담아 포장합니다.
#  - 상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.

# 과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.
# (사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)

# 예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면,
# 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.
#  - (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8

# 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때,
# 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
#========================
k1 = 3
m1 = 4
score1 = [1,2,3,1,2,3,1]
result1 = 8
k2 = 4
m2 = 3
score2 = [4,1,2,2,4,4,4,4,1,2,4,2]
print(sorted(score2, reverse = True))
result2 = 33
def solution(k, m, score):
    answer = 0
    score.sort()
    boxes = len(score) // m
    for i in range(0,boxes):
        box = []
        for j in range(0,m):
            box.append(score.pop())
        answer += min(box) * m
    return answer
print(solution(k1, m1, score1))
print(solution(k2, m2, score2))
print(bool(8 and 41))