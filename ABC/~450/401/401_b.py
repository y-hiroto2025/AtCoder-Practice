"""
問題URL: https://atcoder.jp/contests/abc401/tasks/abc401_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    log = False
    ans = 0

    for _ in range(N):
        s = input().strip()

        if s == "login":
            log = True
        if s == "logout":
            log = False

        if s == "private" and not log:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()