#========================
# 행렬 테두리 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/77485
#========================
rows1 = 6
columns1 = 6
queries1 = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
result1 = [8, 10, 25]
rows2 = 3
columns2 = 3
queries2 = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
result2 = [1, 1, 5, 3]
rows3 = 100
columns3 = 97
queries3 = [[1,1,100,97]]
result3 = 1
def solution(rows, columns, queries):
    answer = []
    table = [[column + (row * columns) for column in range(1, columns + 1)] for row in range(rows)]
    for query in queries:
        tmp = []
        startRow, startCol, endRow, endCol = [i-1 for i in query]
        
        # 사각형 모양을 왼쪽 위 부터 한 칸씩 순회하면서 현 위치의 값을 배열에 저장하고, 저장되어 있는 배열에서 이전 칸의 값을 불러와 대입
        for i in range(startCol, endCol+1):
            tmp.append(table[startRow][i])
            if len(tmp)>1:
                table[startRow][i] = tmp[-2]
            
        for i in range(startRow+1, endRow+1):
            tmp.append(table[i][endCol])
            table[i][endCol] = tmp[-2]
            
        for i in range(endCol-1, startCol-1, -1):
            tmp.append(table[endRow][i])
            table[endRow][i] = tmp[-2]
            
        for i in range(endRow-1, startRow-1, -1):
            tmp.append(table[i][startCol])
            table[i][startCol] = tmp[-2]
        answer.append(min(tmp))
    return answer
print(solution(rows1, columns1, queries1))
print(solution(rows2, columns2, queries2))
print(solution(rows3, columns3, queries3))