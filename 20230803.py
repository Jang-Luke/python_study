#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 주자 요금 계산
#========================
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = [14600, 34400, 5000]
import math
from collections import defaultdict
def solution(fees, records):
    # 차량 입출입 기록을 시간, 차번, 입-출입 여부로 나눔
    records = [record.split() for record in records]
    
    # 나누어진 입출입 기록을 차번별로 정리
    # times = {r[1]:[] for r in records} // defaultdict 를 사용하지 않았을 때가 시행속도는 미세하게 더 빠름
    times = defaultdict(list)
    for r in records:
        times[r[1]] += [r[0]]
    
    for key, value in times.items():
        count = len(value)
        total = 0
        # 입출입 기록이 짝수일 때
        if count % 2 == 0:
            for t in range(0,count,2):
                inHour, inMinute = value[t].split(":")
                outHour, outMinute = value[t+1].split(":")
                total += ((int(outHour)*60) + int(outMinute)) - ((int(inHour)*60) + int(inMinute))
        # 입출입 기록이 홀수일 때 (차량이 나가지 않은 경우)
        else:
            for t in range(0,count-1,2):
                inHour, inMinute = value[t].split(":")
                outHour, outMinute = value[t+1].split(":")
                total += ((int(outHour)*60) + int(outMinute)) - ((int(inHour)*60) + int(inMinute))
            lastHour, lastMinute = value[-1].split(":")
            total += ((24*60)-1) - ((int(lastHour)*60) + int(lastMinute))
        times[key] = total
        
    # 차번이 작은 순으로 요금 계산
    return [fees[1] if time < fees[0] else fees[1] + (math.ceil((time - fees[0]) / fees[2]) * fees[3]) for carNum, time in sorted(times.items())]
print(solution(fees, records))