# 1. 뭔가 간단한 방법이 생각 안남
# 2. x와 y를 따로 비교한다.
# 3. x값중 한개만 있으면 그 값이 찾으려는 점의 x, y도 마찬가지

# count함수를 알면 코드가 간결해진다.
# 아이디어는 같음
X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)
