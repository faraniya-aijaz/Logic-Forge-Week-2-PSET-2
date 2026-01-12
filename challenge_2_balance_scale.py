# def can_balance_scales(arr):
#     total = sum(arr)
#     if total % 2 != 0:
#         return False

#     target = total // 2

#     def check(i, s):
#         if s == target:
#             return True
#         if i == len(arr) or s > target:
#             return False

#         return check(i + 1, s + arr[i]) or check(i + 1, s)

#     return check(0, 0)
# print(can_balance_scales([1, 5, 11, 5]))
# print(can_balance_scales([1, 3, 5]))

def can_balance_scales(arr):
    total = sum(arr)
    
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for weight in arr:
        for s in range(target, weight - 1, -1):
            dp[s] = dp[s] or dp[s - weight]

    return dp[target]
print(can_balance_scales([1, 5, 11, 5]))
print(can_balance_scales([1, 3, 5]))
