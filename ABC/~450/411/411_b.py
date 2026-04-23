"""
問題URL: https://atcoder.jp/contests/abc411/tasks/abc411_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    D = list(map(int, input().split()))

    for i in range(N-1):
        ans = [D[i]]

        for j in range(i+1, N-1):
            ans.append(ans[-1] + D[j])

        print(*ans)   


if __name__ == "__main__":
    main()