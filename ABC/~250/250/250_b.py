"""
問題URL: https://atcoder.jp/contests/abc250/tasks/abc250_b
----------------------------------------------------
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())

    for i in range(N):

        for _ in range(A):
            line = ""

            for j in range(N):

                if (i + j) % 2 == 0:
                    line += "." * B
                else:
                    line +=  "#" * B
            
            print(line)

if __name__ == "__main__":
    main()