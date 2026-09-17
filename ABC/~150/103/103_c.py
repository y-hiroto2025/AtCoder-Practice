"""
問題URL: https://atcoder.jp/contests/abc103/tasks/abc103_c
----------------------------------------------------
結果
・8min
----------------------------------------------------
"""
import sys,math

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    lcm = math.lcm(*A)
    ans = sum([(lcm-1) % a for a in A])
    print(ans)


if __name__ == "__main__":
    main()