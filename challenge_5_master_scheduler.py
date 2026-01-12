# def min_cancel(intervals):
#     def go(i, cur):
#         if i == len(intervals):
#             for j in range(1, len(cur)):
#                 if cur[j][0] < cur[j-1][1]:
#                     return 0
#             return len(cur)
#         return max(go(i+1, cur + [intervals[i]]), go(i+1, cur))
    
#     return len(intervals) - go(0, [])

# print(min_cancel([[1,2],[2,3],[3,4],[1,3]]))  
# print(min_cancel([[1,3],[1,3],[1,3]]))        
# print(min_cancel([[1,2],[5,10],[18,35]]))   
def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    def end_time(x):
        return x[1]

    intervals.sort(key=end_time)  # sort by end time
    end = intervals[0][1]
    remove = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            remove += 1
        else:
            end = intervals[i][1]

    return remove

print(min_cancelled_bookings([[1,2],[2,3],[3,4],[1,3]]))  
print(min_cancelled_bookings([[1,3],[1,3],[1,3]]))       
print(min_cancelled_bookings([[1,2],[5,10],[18,35]]))    
