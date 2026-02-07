"""
問題URL: https://atcoder.jp/contests/abc374/tasks/abc374_c
----------------------------------------------------
----------------------------------------------------
"""
import sys
import itertools

input = sys.stdin.readline

def main():
    N = int(input())
    K = list(map(int, input().split()))

    ans = float('inf')
    total_K = sum(K)

    for pattern in itertools.product([0, 1], repeat=N):
        S_A = sum(list(K[i] * pattern[i] for i in range(N)))
        S_B = total_K - S_A

        current_score = max(S_A, S_B)

        ans = min(ans, current_score)
    print(ans)


if __name__ == "__main__":
    main()