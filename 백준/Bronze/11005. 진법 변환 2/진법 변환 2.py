# 저렇게 형변환 chr(),ord()말고 써서 할 수 있을텐데 찾아봐야겠다.
# 슬라이싱 한번 다시 기억해주고
# 원리 : 10진수를 B(몇진법)으로 나누면 그 나머지가 차례로 변환이 되는것이다.
#       문자일때랑 숫자일때만 구분해서 해주자.
N, B = map(int, input().split())
B = B
s = ""
while N > 0:
    remainder = N % B
    N = N // B
    if remainder < 10:
        s += chr(remainder + ord('0'))
    elif remainder >= 10:
        s += chr((remainder - 10) + ord('A'))
print(s[::-1])