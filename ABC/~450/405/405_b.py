"""
問題URL: https://atcoder.jp/contests/abc405/tasks/abc405_b
----------------------------------------------------
結果
・自力（8min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    M_list = [i for i in range(1, M + 1)]

    ans = 0
    while True:
        for i in range(1, M + 1):
            if i not in A:
                print(ans)
                return
            
        A.pop(-1)
        ans += 1

if __name__ == "__main__":
    main()