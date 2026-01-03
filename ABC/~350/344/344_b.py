"""
問題URL: https://atcoder.jp/contests/abc344/tasks/abc344_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    A = []
    while True:
        A.append(int(input()))
        if A[-1] == 0:
            break
    
    """
    for i in range(len(A)):
        print(A[-i - 1])
    """
    """
    for a in A[::-1]:
        print(a)
    """

    print(*A, sep='\n')


if __name__ == "__main__":
    main()