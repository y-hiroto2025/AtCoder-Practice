"""
問題URL: https://atcoder.jp/contests/abc464/tasks/abc464_a
----------------------------------------------------
結果
・1min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    S = input().strip()

    E_cnt, W_cnt = 0, 0

    for s in S:
        if s == "E":
            E_cnt+=1
        else:
            W_cnt+=1
    
    if E_cnt>W_cnt:
        print("East")
    else:
        print("West")


if __name__ == "__main__":
    main()