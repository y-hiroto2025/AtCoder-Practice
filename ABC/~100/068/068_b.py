"""
問題URL: https://atcoder.jp/contests/abc068/tasks/abc068_b
----------------------------------------------------
結果
・7min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    ans = 1
    curr_max = 0

    for i in range(1, N+1):
        num = i
        tmp = 0

        while num % 2 == 0:
            num = num // 2
            tmp += 1

        if tmp > curr_max:
            curr_max = tmp
            ans = i

    print(ans)


if __name__ == "__main__":
    main()