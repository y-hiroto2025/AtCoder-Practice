"""
問題URL: https://atcoder.jp/contests/abc262/tasks/abc262_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    same_num = [i+1 for i in range(N) if A[i] == i+1]
    same_cnt = len(same_num)

    ans += same_cnt * (same_cnt-1) // 2

    confirmed_num = set()
    for i in range(N):
        if (A[i] != i+1) and (A[A[i]-1] == i+1) and (i+1 not in confirmed_num):
            confirmed_num.add(A[i])
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()