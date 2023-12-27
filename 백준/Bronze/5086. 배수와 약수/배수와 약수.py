# 입력 값의 사이즈가 얼마나 되는지 모를때는
# sys.stdin의 readlines()로 파일을 한번에 읽을 수 있다.
# 그런데 문제를 잘 안읽어서 끝에 0 0 이라는 끝을 알려주는 데이터가
# 들어오는 것을 나중에 알았다. 아무튼
# 1. 끝을 모를때는 readlines() 사용하기
# 2. 이 문제는 그냥 약수 배수의 정의 알기
import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    if A == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
