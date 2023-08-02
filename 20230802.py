#========================
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기
#========================
n1 = 437674
k1 = 3
result1 = 3
n2 = 110011
k2 = 10
result = 2

# 진법 변환 함수
def convert(num, base):
    nums = "0123456789"
    q, r = divmod(num, base)
    if q == 0 :
        return nums[r] 
    else :
        return convert(q, base) + nums[r]
    
def solution(n, k):
    answer = 0
    
    # 전체 숫자 리스트
    primeNums = convert(n,k).split("0")
    
    # 소수 판별
    for i in primeNums:
        
        # 00 처럼 0이 연속으로 오는 경우 '' (공백) 이므로 제외
        if i:
            isPrime = True
            num = int(i)
            for j in range(2, int(num**0.5+1)):
                if num % j == 0:
                    isPrime = False
                    break
            
            # 010 같은 경우를 산정해 1을 제외
            if isPrime and num != 1: answer += 1
    return answer
print(solution(n1, k1))
print(solution(n2, k2))