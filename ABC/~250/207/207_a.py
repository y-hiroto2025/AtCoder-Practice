# 問題URL: https://atcoder.jp/contests/abc207/tasks/abc207_a

def main():
    nums = list(map(int, input().split()))
    nums.sort()

    ans = nums[-1] + nums[-2]
    print(ans)

"""
ans = sum(nums) - min(nums)
"""


if __name__ == "__main__":
    main()