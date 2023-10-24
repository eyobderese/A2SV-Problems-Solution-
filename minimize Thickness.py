from typing import List


class OS:
    def __init__(self):
        self.tree = []

    def insert(self, val):
        self.tree.append(val)

    def order_of_key(self, val):
        count = 0
        for num in self.tree:
            if num < val:
                count += 1
        return count


class OMS:
    def __init__(self):
        self.tree = []

    def insert(self, val):
        self.tree.append(val)

    def order_of_key(self, val):
        count = 0
        for num in self.tree:
            if num <= val:
                count += 1
        return count


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = n
        segSum = 0

        for i in range(n):
            segSum += a[i]
            s = 0
            length = 0
            maxLen = i + 1
            possible = False
            for j in range(i + 1, n):
                if s + a[j] > segSum:
                    break
                if j == n - 1 and s + a[j] == segSum:
                    maxLen = max(maxLen, length + 1)
                    possible = True
                    break
                s += a[j]
                length += 1
                if s == segSum:
                    maxLen = max(maxLen, length)
                    length = 0
                    s = 0
            if possible:
                ans = min(ans, maxLen)

        print(ans)


if __name__ == '__main__':
    main()
