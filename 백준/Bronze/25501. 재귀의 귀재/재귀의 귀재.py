# 재귀로 작성된 펠린드롬확인 함수의 호출횟수 확인하기
# count class를 통해서 solution함수의 호출횟수를 알아낸다.
class C:
    count = 0

def solution(s,l,r, c):
    c.count += 1
    if l >= r: return 1
    elif s[l] != s[r] : return 0
    else: return solution(s,l+1,r-1, c)
def isPalindrome(s,c):
    return solution(s,0,len(s)-1,c)


N = int(input())
c = C()
for _ in range(N):
    c.count = 0
    print(isPalindrome(input().rstrip(),c), c.count)