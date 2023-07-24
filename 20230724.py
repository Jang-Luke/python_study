#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 이모티콘 할인행사
#========================
users1 = [[40, 10000],[25,10000]]
emoticons1 = [7000, 9000]
result1 = [1, 5400]
users2 = [[40, 2900],[23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons2 = [1300, 1500, 1600, 4900]
result2 = [4, 13860]

# from itertools import product

# def solution(users, emoticons):
#     answer = [0, 0]
#     percents = [10, 20, 30, 40]
#     # 모든 경우의 수
#     discounts = list(product(percents, repeat=len(emoticons)))
#     for discount in discounts:
#         join = 0
#         price = 0
#         # 유저별 계산
#         for user in users:
#             pay = 0
#             for i in range(len(emoticons)):
#                 if user[0] <= discount[i]:
#                     pay += emoticons[i] * (100 - discount[i])/100
#                 if pay >= user[1]:
#                     break
#             if pay >= user[1]:
#                 pay = 0
#                 join += 1
#             price += pay
#         # 가입과 금액 비교후 변경
#         if join > answer[0]:
#             answer = [join, price]
#         elif join == answer[0]:
#             answer[1] = max(answer[1], price)
#     return answer