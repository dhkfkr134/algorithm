# 1. 약수구하기문제 + 여러 케이스처리 + 문자열or배열(데이터)관리
# 2. 입력값 한줄마다 약수들을 구해야한다. 이중반복문
# 3. 약수들을 합한값을 기록하고, 그 약수들도 기록해야한다
# 4. 본인을 제외한 약수들의 합이 본인과 같으면(완전수이면) 기록한 약수들 출력
# 5. 아니면 is NOT perfect. 출력
import sys
lines = sys.stdin.readlines()
for line in lines:
    line = int(line)
    string = f'{line} = 1'
    sum = 0

    if line == -1:
        break
    for i in range(1, line):
        if line % i == 0:
            if i != 1:
                string += f' + {i}'
                sum += i
            else:
                sum += 1
    if sum == line:
        print(string)
    else:
        print(f'{line} is NOT perfect.')