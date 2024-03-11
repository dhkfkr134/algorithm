count = int(input())
nums = list(map(int,input().split()))
isOdd = True
# 약수에 2가 있거나, 약수가 모두 홀수 이거나라면
for num in nums:
    if (num & 1) is 0:
        isOdd = False
        break
if isOdd:
    print(max(nums)*min(nums))
else:
    print(max(nums)*2)