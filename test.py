"""
url: https://atcoder.jp/contests/agc019/tasks/agc019_a
"""

import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    total_length = sum(A)
    sum_left = 0
    min_diff = float('inf')

    for i in range(N-1):
        sum_left += A[i]
        sum_right = total_length - sum_left

        diff = abs(sum_left - sum_right)
        min_diff = min(min_diff, diff)

    print(min_diff)


if __name__ == "__main__":
    main()