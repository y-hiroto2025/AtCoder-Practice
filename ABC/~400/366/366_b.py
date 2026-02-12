"""
問題URL: https://atcoder.jp/contests/abc367/tasks/abc367_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    max_len = 0
    S = []
    for _ in range(N):
        S_i = input().strip()
        S.append(S_i)
        max_len = max(max_len, len(S_i))

    ans = [["*"] * N for _ in range(max_len)]

    for i in range(max_len):
        for j in range(N):
            if i < len(S[j]):
                ans[i][j] = S[j][i]
        row_str = reversed(ans[i])
        row_str = "".join(row_str)

        print(row_str.rstrip("*"))

if __name__ == "__main__":
    main()