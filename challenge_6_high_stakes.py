# def maximize_freelance_profit(d, p):
#     n = len(d)
#     jobs = list(zip(p, d))
#     jobs.sort(reverse=True)
    
#     max_d = max(d)
#     slot = [0] * (max_d + 1)
    
#     done = 0
#     earn = 0

#     for pay, ddl in jobs:
#         for h in range(ddl, 0, -1):
#             if slot[h] == 0:
#                 slot[h] = 1
#                 done += 1
#                 earn += pay
#                 break

#     return [done, earn]
# print(maximize_freelance_profit([4,1,1,1], [20,10,40,30]))
# print(maximize_freelance_profit([2,1,2,1,1], [100,19,27,25,15]))

def maximize_freelance_profit(deadlines, profits):
    n = len(deadlines)
    jobs = list(zip(profits, deadlines))
    jobs.sort(reverse=True) 
    
    max_deadline = max(deadlines)
    slots = [0] * (max_deadline + 1) 
    
    total_jobs = 0
    total_profit = 0

    for profit, deadline in jobs:
        for hour in range(deadline, 0, -1): 
            if slots[hour] == 0:  
                slots[hour] = 1  
                total_jobs += 1
                total_profit += profit
                break 

    return [total_jobs, total_profit]
print(maximize_freelance_profit([4, 1, 1, 1], [20, 10, 40, 30]))
print(maximize_freelance_profit([2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))
