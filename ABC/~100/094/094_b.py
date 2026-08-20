"""
問題URL: https://atcoder.jp/contests/abc094/tasks/abc094_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    left=0
    right=0

    for a in A:
        if a<X:
            left+=1
        else:
            right+=1

    ans = min(left, right)

    print(ans)

if __name__ == "__main__":
    main()