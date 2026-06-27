"""
問題URL: https://atcoder.jp/contests/abc285/tasks/abc285_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()

    ans = 0
    std = ord("A") - 1

    for i in range(len(S)):
        keta = 26**(len(S) - i-1)

        ans += (ord(S[i]) - std) * keta
    
    print(ans)

if __name__ == "__main__":
    main()