def solution(ns, target):
    ns.sort()
    left = 0
    right = len(ns)-1
    while left < right:
        if ns[right] >= target:
            right -= 1
            continue
        if ns[left]+ns[right] < target:
            left += 1
        elif ns[left] + ns[right] > target:
            right -= 1
        else:
            return ns[left],ns[right]

nums = [7, 3, 2, 13, 9, 15, 8, 11]
print(solution(nums,12))