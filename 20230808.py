#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/92342
# 양궁 대회
#========================
n1 = 5
info1 = [2,1,1,1,0,0,0,0,0,0,0]
result1 = [0,2,2,0,1,0,0,0,0,0,0]
n2 = 1
info2 = [1,0,0,0,0,0,0,0,0,0,0]
result2 = [-1]
n3 = 9
info3 = [0,0,1,2,0,1,1,1,1,1,1]
result3 = [1,1,2,0,1,2,2,0,0,0,0]
n4 = 10
info4 = [0,0,0,0,0,0,0,0,3,4,3]
result4 = [1,1,1,1,1,1,1,1,0,0,2]
from itertools import product
def solution(n, info):
    answer = [-1]
    
    # 어피치, 라이언 점수
    apeachScore = sum([j for i, j in enumerate(range(10, 0, -1)) if info[i] > 0])
    ryanScore = 0
    
    diff = 0
    lastIdx = 0
    
    for result in product((True, False), repeat = 11):
        ryanInfo = [0] * 11
        a, r = apeachScore, ryanScore
        tmpLastIdx = 0
        count = n
        # result = (T,F,T,F ...) 라이언의 화살이 어피치의 화살보다 많을 경우 T, 아닐경우 F
        for i, v in enumerate(range(10, -1, -1)):
            if result[i]:
                
                # 라이언의 화살이 어피치의 화살보다 더 많이 맞은 경우
                if info[i]:
                    a -= v
                    r += v
                    tmpLastIdx = i
                
                #라이언의 화살만 맞은 경우
                else:
                    r += v
                
                # 점수별 라이언이 쏜 화살의 갯수 입력
                requiredArrow = info[i] + 1
                ryanInfo[i] = requiredArrow
                
                # 남아있는 화살 계산
                if count - requiredArrow > -1:
                    count -= requiredArrow
            
            # 0점이 될 때 까지 반복하고 남은 화살은 0점에 입력
            elif v == 0 and count != 0:
                ryanInfo[i] = count
                
        # 점수표에 입력된 화살의 개수가 n 이고, 라이언과 어피치의 점수 차가 기존보다 더 큰 경우 리턴 값 변경
        if sum(ryanInfo) == n:
            tmpDiff = r - a
            if tmpDiff > diff:
                diff = tmpDiff
                answer = ryanInfo
                lastIdx = tmpLastIdx
            # 동점이라면 낮은 점수를 많이 맞춘쪽이 우선
            elif tmpDiff == diff:
                if lastIdx < tmpLastIdx:
                    answer = ryanInfo
                    
                # elif lastIdx == tmpLastIdx:
                #     if answer[lastIdx] <= ryanInfo[tmpLastIdx]:
                #         answer = ryanInfo
    return answer

print(solution(n1, info1))
print(solution(n2, info2))
print(solution(n3, info3))
print(solution(n4, info4))

# 8, 18 케이스 실패



# 라이언이 화살을 n 번 쏘는 모든 경우의 수를 구하는 중 ... product를 쓰는게 맞아 보이는데 case 수가 너무 많다.
# from itertools import combinations_with_replacement
# ex = combinations_with_replacement([i for i in range(11)], 10)
# exR = combinations_with_replacement([i for i in range(10,-1,-1)], 10)
# count = 0
# for i in ex:
#     if sum(i) < 11:
#         print(i)
#     count += 1
# for i in exR:
#     if sum(i) < 11:
#         print(i)
#     count += 1
# print(count)
# print([i for i in range(10,-1,-1)])