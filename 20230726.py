#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기
#========================
survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]
result1 = "TCMA"
survey2 = ["TR", "RT", "TR"]
choices2 = [7, 1, 3]
result2 = "RCJA"
def solution(survey, choices):
    answer = ''
    score = [0,1,2,3]
    types = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    sc1 = ["",0]
    sc2 = ["",0]
    index = 0
    
    # 점수 매기기
    for i in range(len(survey)):
        calcScore = choices[i] - 4
        if calcScore > 0:
            types[survey[i][1]] += score[abs(calcScore)]
        elif calcScore < 0:
            types[survey[i][0]] += score[abs(calcScore)]
    
    # 2개씩 비교
    for key, value in types.items():
        if index % 2 == 0:
            sc1 = [key, value]
        else:
            sc2 = [key, value]
            if sc1[1] < sc2[1]:
                answer += sc2[0]
            else:
                answer += sc1[0]
        index += 1
    return answer
print(solution(survey1, choices1))
print(solution(survey2, choices2))