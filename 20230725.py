#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 택배 배달과 수거하기
#========================
cap1 = 4
n1 = 5
deliveries1 = [1,0,3,1,2]
pickups1 = [0,3,0,4,0]
result1 = 16
cap2 = 2
n2 = 7
deliveries2 = [1,0,2,0,1,0,2]
pickups2 = [0,2,0,1,0,2,0]
result2 = 30
def solution(cap, n, deliveries, pickups):
    answer = 0
    count = 0
    loopFlag = False
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        # 최대 거리
        distance = max(len(deliveries), len(pickups))
        for i in range(1, len(deliveries) + 1):
            if loopFlag:
                loopFlag = False
                break
            if len(deliveries) == 0: break
            while(deliveries[-i] != 0):
                deliveries[-i] -= 1
                count += 1
                # distance.append(n - i + 1)
                if count == cap:
                    count = 0
                    loopFlag = True
                    break
            if i == len(deliveries):
                count = 0
                loopFlag = False
                break
        for i in range(1, len(pickups) + 1):
            if loopFlag: 
                loopFlag = False
                break
            if len(pickups) == 0: break
            while(pickups[-i] != 0):
                pickups[-i] -= 1
                count += 1
                # distance.append(n - i + 1)
                if count == cap:
                    count = 0
                    break
            if i == len(deliveries):
                count = 0
                break
        answer += distance*2
    return answer
print(solution(cap1, n1, deliveries1, pickups1))
print(solution(cap2, n2, deliveries2, pickups2))



# def solution(cap, n, deliveries, pickups):
#     answer = 0

#     while deliveries or pickups:
#         # 맨뒤 0 제거
#         while deliveries and deliveries[-1] == 0:
#             deliveries.pop()
#         while pickups and pickups[-1] == 0:
#             pickups.pop()
#         # 최대 거리
#         distance = max(len(deliveries), len(pickups))

#         # 배송
#         delivery = cap
#         while deliveries and delivery > 0:
#             boxs = deliveries.pop()
#             if boxs <= delivery:
#                 delivery -= boxs
#             else:
#                 deliveries.append(boxs - delivery)
#                 break

#         # 픽업
#         pickup = cap
#         while pickups and pickup > 0:
#             boxs = pickups.pop()
#             if boxs <= pickup:
#                 pickup -= boxs
#             else:
#                 pickups.append(boxs - pickup)
#                 break

#         # 거리 증가
#         answer += distance * 2
#     return answer