"""
問題URL: https://atcoder.jp/contests/abc343/tasks/abc343_c
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans_set = set()
    for i in range(1000000):
        K = i ** 3
        if K > N:
            break
        else:
            if str(K) == str(K)[::-1]:
                ans_set.add(K)
    print(max(ans_set))

if __name__ == "__main__":
    main()