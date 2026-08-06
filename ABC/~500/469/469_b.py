"""
問題URL: https://atcoder.jp/contests/abc469/tasks/abc469_b
----------------------------------------------------
結果
・8min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    S = input().strip()
    S = "x" + S + "x"

    ans = 0

    for i in range(1, N+1):
        if S[i-1]=="x" and S[i]=="x" and S[i+1]=="x":
            ans += 1    

    print(ans)

if __name__ == "__main__":
    main()