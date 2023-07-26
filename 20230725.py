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
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    # 배열 역순으로 뒤집기
    answer = 0

    delivery_box = 0
    pickup_box = 0
    # 배달 or 픽업 해야할 택배 갯수 (끝 거리부터 추가하면서 계산)
    for i in range(n):
        delivery_box += deliveries[i]
        pickup_box += pickups[i]
        # n - i 거리의 택배 갯수를 더하여
        while delivery_box > 0 or pickup_box > 0:
            delivery_box -= cap
            pickup_box -= cap
            answer += (n - i) * 2
        # 그 값이 cap 보다 작은 경우, 최대거리에 2배를 계산
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