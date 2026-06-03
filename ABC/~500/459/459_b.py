"""
問題URL: https://atcoder.jp/contests/abc459/tasks/abc459_b
----------------------------------------------------
結果
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    S = input().split()

    C = []
    
    for i in range(N):
        if S[i][0] in "abc":
            C.append(2)
        elif S[i][0] in "def":
            C.append(3)
        elif S[i][0] in "ghi":
            C.append(4)
        elif S[i][0] in "jkl":
            C.append(5)
        elif S[i][0] in "mno":
            C.append(6)
        elif S[i][0] in "pqrs":
            C.append(7)
        elif S[i][0] in "tuv":
            C.append(8)
        elif S[i][0] in "wxyz":
            C.append(9)
    
    print(*C, sep="")



if __name__ == "__main__":
    main()