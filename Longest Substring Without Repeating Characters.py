def lengthOfLongestSubstring(s):
    longest, i, j = 0, 0, 0
    areDistinict = True
    while j < len(s):
        if s[j] not in s[i:j]:
            j += 1

        else:
            print("i: ", i, "j: ", j)

            longest = max(longest, j-i)
            i += 1
            areDistinict = False
    longest = max(longest, j-i)
    return len(s) if areDistinict else longest


print(lengthOfLongestSubstring("aaaab"))
