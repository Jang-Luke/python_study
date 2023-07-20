#========================
# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3
#========================
import datetime as dt
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# datetime.datetime(2020, 10, 2, 15, 27, 4, 517207)
def solution(today, terms, privacies):
    answer = []
    dtToday = parse(today)
    dicTerms = {}
    for e in terms:
        parseTerms = e.split(" ")
        dicTerms[parseTerms[0]] = int(parseTerms[1])
    for index, value in enumerate(privacies):
        privacy = value.split(" ")
        dtPrivacy = parse(privacy[0])
        delCriteria = dtPrivacy + relativedelta(months=dicTerms[privacy[1]])
        if (delCriteria - dtToday).days <= 0:
            answer.append(index+1)
    return answer
print(solution(today, terms, privacies))