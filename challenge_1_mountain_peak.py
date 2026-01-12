# def ways(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return ways(n - 1) + ways(n - 2)
# print(ways(2))
# print(ways(3))
# print(ways(4))
# print(ways(5))
# print(ways(45))

def count_climbing_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
print("Total unique ways",count_climbing_ways(2))
print("Total unique ways",count_climbing_ways(3))
print("Total unique ways",count_climbing_ways(4))
print("Total unique ways",count_climbing_ways(5))
print("Total unique ways",count_climbing_ways(45))
