# 목표값에서 0까지 내려갈지, 0에서 목표값까지 도달하게 할지
# 어떤방식이 간단한 코딩이 되는지 생각하면서 하기
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)
