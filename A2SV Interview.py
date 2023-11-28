

# """
# Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.


# Example 1:
# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.


# Example 2:
# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

# Constraints:
# 1 <= s.length <= 10**4
# s consists of lowercase English letters.
# 1 <= k <= 10**4
# """

from collections import defaultdict


def myFunction(s, k):
    tracker = defaultdict(int)
    n = len(s)
    counter = 0

    minRange = min(n, k)

    for i in range(minRange):
        tracker[s[i]] += 1

    j = 0
    for i in range(k, n):

        if len(tracker) == k:
            counter += 1

        tracker[s[j]] -= 1  # tracker[s[i-k]]-=1
        tracker[s[i]] += 1

        if tracker[s[j]] == 0:
            del tracker[s[j]]

        j += 1

    if len(tracker) == k:
        counter += 1
    return counter


print(myFunction("havefunonleetcode", 5))
