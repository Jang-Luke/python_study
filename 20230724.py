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
def solution(users, emoticons):
    answer = []
    rates = [i[0]//10*10 for i in users]
    price = 0
    priceList = {}
    purchaseCnt = {i * 10 : len(list(filter(lambda x : x <= i*10, rates))) for i in range(1, 5)}
    for index, emoticon in enumerate(emoticons):
        price += max([emoticon * ((100 - i) / 100) * purchaseCnt[i] for i in [40,30,20,10]])
        priceList[index] = {i:emoticon * ((100 - i) / 100) * purchaseCnt[i] for i in [40,30,20,10]}
        print(f"{index} : {max([emoticon * ((100 - i) / 100) * purchaseCnt[i] for i in [40,30,20,10]])}")
    
    return purchaseCnt
print(solution(users2, emoticons2))