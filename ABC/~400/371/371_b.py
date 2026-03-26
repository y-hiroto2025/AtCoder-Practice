"""
問題URL: https://atcoder.jp/contests/abc371/tasks/abc371_b
----------------------------------------------------
結果
・自力（4min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    h = {str(i+1): False for i in range(N)}

    for _ in range(M):
        a, b = input().split()

        if not h[a] and b == "M":
            print("Yes")
            h[a] = True
        else:
            print("No")    


if __name__ == "__main__":
    main()