"""
問題URL: https://atcoder.jp/contests/abc463/tasks/abc463_b
----------------------------------------------------
結果
・3min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, X = input().split()
    N = int(N)
    x = {"A":0, "B": 1, "C": 2, "D": 3, "E": 4}[X]

    ans = "No"

    for _ in range(N):
        s = input().strip()
        if s[x] == "o":
            ans = "Yes"
    
    print(ans)


if __name__ == "__main__":
    main()