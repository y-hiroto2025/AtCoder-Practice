"""
問題URL: https://atcoder.jp/contests/abc209/tasks/abc209_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    C = sorted(map(int, input().split()))

    ans = 1
    i = 0
    for c in C:
        ans *= c - i
        i += 1
        ans %= 10**9 + 7
        
    print(ans)

if __name__ == "__main__":
    main()