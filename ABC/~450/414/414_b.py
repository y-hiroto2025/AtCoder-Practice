"""
問題URL: https://atcoder.jp/contests/abc414/tasks/abc414_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N = int(input())

    ans = ""
    len_ans = 0

    c_l = []
    for _ in range(N):
        c, l = input().split()
        l = int(l)
        len_ans += l

        c_l.append((c, l))

    if len_ans > 100:
        print("Too Long")
        return
    
    for i in range(N):
        ans += c_l[i][0] * c_l[i][1]
    
    print(ans)



if __name__ == "__main__":
    main()