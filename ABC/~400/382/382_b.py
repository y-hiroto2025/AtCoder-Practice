"""
問題URL: https://atcoder.jp/contests/abc382/tasks/abc382_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, D = map(int, input().split())
    S = [s for s in input().strip()]

    cnt = 0
    for i in range(N):
        if S[N-i - 1] == "@":
            cnt += 1
            S[N-i - 1] = "."
        
        if cnt == D:
            break
    
    print(*S, sep="")


if __name__ == "__main__":
    main()