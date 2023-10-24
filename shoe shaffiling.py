
from collections import defaultdict


def prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        br = [i for i in range(1, n+1)]
        mp = defaultdict(int)
        v = []
        ans = 0
        for i in range(n-1):
            if ar[i] == ar[i+1]:
                v.append(br[i+1])
                br[i], br[i+1] = br[i+1], br[i]
                mp[i] += 1
                mp[i+1] += 1
            else:
                if mp[i] != 0:
                    v.append(br[i])
                else:
                    ans = 1
                    break
        if mp[n-1] != 0:
            v.append(br[n-1])
        else:
            ans = 1
        if ans == 1:
            print("-1")
        else:
            print(*v)


if __name__ == "__main__":
    main()
