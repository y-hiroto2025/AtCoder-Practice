"""
問題URL: https://atcoder.jp/contests/abc372/tasks/abc372_c
----------------------------------------------------
結果
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    S = input().strip()

    ans = S.count("ABC")
    S = list(S)


    for _ in range(Q):
        x_str, c = input().split()
        x = int(x_str) - 1

        for i in range(x, x+3):
            if 0 <= i-2 and i < N:
                if S[i-2] == "A" and S[i-1] == "B" and S[i] == "C":
                    ans -= 1
        
        S[x] = c

        for i in range(x, x+3):
            if 0 <= i-2 and i < N:
                if S[i-2] == "A" and S[i-1] == "B" and S[i] == "C":
                    ans += 1
        
        print(ans)


if __name__ == "__main__":
    main()