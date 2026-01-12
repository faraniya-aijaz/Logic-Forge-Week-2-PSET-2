# import math

# def calculate_minimum_speed(piles, k):
#     low = 1
#     high = max(piles)
#     result = high
    
#     while low <= high:
#         mid = (low + high) // 2
#         hours_needed = 0
        
#         for pile in piles:
#             hours_needed += math.ceil(pile / mid)
        
#         if hours_needed <= k:
#             result = mid
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     return result

# print(calculate_minimum_speed([5, 10, 3], 4))   
# print(calculate_minimum_speed([5, 10, 15, 20], 7))  

def calculate_minimum_speed(piles, k):
    low, high = 1, max(piles)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        hours_needed = 0
        
        for pile in piles:
            hours_needed += (pile + mid - 1) // mid
        
        if hours_needed <= k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

print(calculate_minimum_speed([5, 10, 3], 4))       
print(calculate_minimum_speed([5, 10, 15, 20], 7))  
