"""
問題URL: https://atcoder.jp/contests/abc093/tasks/abc093_c
----------------------------------------------------
結果
・9min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    nums = sorted(map(int, input().split()), reverse=True)
    ans = 0

    if (nums[1] - nums[2]) % 2 != 0:
        nums[0] += 1
        nums[1] += 1
        ans += 1

    ans += (nums[1] - nums[2]) // 2 + nums[0] - nums[1]

    print(ans)

if __name__ == "__main__":
    main()