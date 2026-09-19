"""
問題URL: https://atcoder.jp/contests/abc079/tasks/abc079_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    nums = input().strip()
    nums = [int(i) for i in nums]
    A,B,C,D = nums[0],nums[1],nums[2],nums[3]

    if A+B+C+D==7:
        ans = "+++"
    elif A+B+C-D==7:
        ans = "++-"
    elif A+B-C+D==7:
        ans = "+-+"
    elif A+B-C-D==7:
        ans = "+--"
    elif A-B+C+D==7:
        ans = "-++"
    elif A-B+C-D==7:
        ans = "-+-"
    elif A-B-C+D==7:
        ans = "--+"
    elif A-B-C-D==7:
        ans = "---"

    print(A,ans[0],B,ans[1],C,ans[2],D,"=7", sep="")


if __name__ == "__main__":
    main()