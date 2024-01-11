# 1. 오름차순정렬하면 자기 왼쪽에 있는 숫자들이 작은 숫자임
# 2. 그런데 중복이 없다면 자신의 index가 왼쪽에 있는 숫자개수임
# 3. 중복이 있으니까 중복될때마다 하나씩 빼주면 됌
# 고민한 점 : 한개의 배열에서 값을 바꾸고 비교하려니까 비교가 안됐다.
#           그래서 새로운 배열을 만들어서 똑같이 값을 바꾸고 비교하는데도 마찬가지였다.
#           생각하다보니 얕은복사개념때문에 그런거같아서 index slicing을 사용했다.
#           그런데 2차원배열에서는 전체 배열만 복사해주고 내용물은 복사해주지 않는점이 있었다.
#           그래서 copy라이브러리에서 deepcopy함수를 사용하려다가 그냥 메모리 키우지말고,
#           임시변수하나를 만들어서 비교하려는 이전값만 담아서 쓰자는 생각이 마지막에서야 났다.
#           결론 1. 리스트도 인스턴스이다. 2. slice는 겉만복사하는 얕은복사이다.

N = int(input())
arr = list(map(int, input().split()))
check = 0
# 입력받기 [i, Xi]
for i in range(N):
    tmp = [i, arr[i]]
    arr[i] = tmp
# [Xi]기준으로 오름차순
arr.sort(key=lambda x: x[1])
# 이전값 비교해줄 변수 ex) arr[i-1][1]
tmp = 0
# 자신의 압축좌표 X'i는 정렬된 현재배열 기준 왼쪽에 있는 수의 갯수 = 자신의 현재배열의 index
# 그러나 중복일 때 체크해서 적용시켜줘야함
for i in range(N):
    if i > 0 and tmp == arr[i][1]:
        check += 1
    tmp = arr[i][1]
    arr[i][1] = i - check

# 다시 [i]기준으로 정렬
arr.sort(key=lambda x: x[0])

for a in arr:
    print(a[1],end=" ")
