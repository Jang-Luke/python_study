#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기
#========================
id_list = ["muzi","frodo","apeach","neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
result = [2,1,1,0]
def solution(id_list, report, k):
    report = [i.split() for i in set(report)]
    users = len(id_list)
    
    # 신고받은 횟수
    count = [0] * users
    
    # 신고한 다른 멤버
    report_list = [[] for id in id_list]
    
    for index, value in enumerate(report):
        count[id_list.index(value[1])] += 1
        report_list[id_list.index(value[0])] += [value[1]]

    # 멤버별 받을 알림의 수
    result = [0] * users
    
    for i, v in enumerate(report_list):
        for j in range(len(v)):
            if count[id_list.index(v[j])] >= k:
                result[i] += 1
    return result
print(solution(id_list, report, k))


def solution2(id_list, report, k):
    # 신고 [유저ID : 유저가 신고한 ID]
    declaration =  {key: set() for key in id_list}
    # 정지 [유저ID : 신고된 횟수]
    stop = {key: 0 for key in id_list}
    # 신고 & 정지 작업
    for re in report:
        id, r_id = re.split(' ', 1)
        # 중복 신고 확인 (set이여서 할 필요는 없지만 중복 정지 증가를 막기위해 추가)
        if r_id not in declaration[id]:
            declaration[id].add(r_id)
            stop[r_id] += 1
    # 정지 중 k 미만 삭제
    ban = [key for key, value in stop.items() if value >= k]
    # 신고 중 정지된 ID 카운트
    return [len(declaration[key].intersection(set(ban))) for key, value in declaration.items()]
print(solution2(id_list, report, k))