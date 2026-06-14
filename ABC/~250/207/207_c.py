"""
問題URL: https://atcoder.jp/contests/abc207/tasks/abc207_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    a = []

    for _ in range(N):
        t, l, r = map(int, input().split())

        if t == 2:
            r -= 0.5
        elif t == 3:
            l += 0.5
        elif t == 4:
            l += 0.5
            r -= 0.5
        
        a.append((l, r))
    
    ans = 0
    
    for i in range(N-1):

        for j in range(i+1, N):

            if max(a[i][0], a[j][0]) <= min(a[i][1], a[j][1]):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()