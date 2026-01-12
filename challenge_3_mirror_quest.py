def find_longest_mirror_length(s):
    def lps_recursive(start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            return 2 + lps_recursive(start + 1, end - 1)
        else:
            return max(lps_recursive(start + 1, end), lps_recursive(start, end - 1))
    
    return lps_recursive(0, len(s) - 1)

print(find_longest_mirror_length("bbabcbcab")) 
print(find_longest_mirror_length("GEEKS"))      
print(find_longest_mirror_length("MAPAM"))      
print(find_longest_mirror_length("ABCD"))       
