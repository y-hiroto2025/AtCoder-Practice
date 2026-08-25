"""
問題URL: https://atcoder.jp/contests/abc079/tasks/abc079_b
----------------------------------------------------
結果
・18min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    if N == 1:
        print(1)
        return
    
    ans = 3
    a = 2
    b = 1

    for _ in range(N-2):
        tmp = b
        b = ans
        a = tmp

        ans = b+a

    print(ans)



if __name__ == "__main__":
    main()