#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 두 큐 합 같게 만들기
#========================
queue1_1 = [3,2,7,2]
queue2_1 = [4,6,5,1]
result_1 = 2
queue1_2 = [1,2,1,2]
queue2_2 = [1,10,1,2]
result_2 = 7
queue1_3 = [1,1]
queue2_3 = [1,5]
result_3 = -1
from collections import deque
def solution(queue1, queue2):
    count = 0
    queue_1 = deque(queue1)
    queue_2 = deque(queue2)
    
    sum_queue1 = sum(queue_1)
    sum_queue2 = sum(queue_2)
    
    # 두 큐의 합이 홀수면 -1 리턴
    if (sum_queue1 + sum_queue2) % 2 == 1:
        return -1
    
    # 최악의 경우를 상정하여 최대 연산 횟수 제한
    limit = len(queue1)*3
    
    # 큐의 합이 같아질 때 까지 합이 더 큰 큐에서 작은 큐로 이동
    # 최대 시행 횟수 limit(3N) 에 도달할 때 까지 두 수의 합이 같아지지 않으면 -1 리턴
    while sum_queue1 != sum_queue2:
        if sum_queue1 > sum_queue2:
            popped = queue_1.popleft()
            queue_2.append(popped)
            sum_queue1 -= popped
            sum_queue2 += popped
            count += 1
        else:
            popped = queue_2.popleft()
            queue_1.append(popped)
            sum_queue1 += popped
            sum_queue2 -= popped
            count += 1
        if count == limit:
            return -1
    return count
print(solution(queue1_1, queue2_1))
print(solution(queue1_2, queue2_2))
print(solution(queue1_3, queue2_3))