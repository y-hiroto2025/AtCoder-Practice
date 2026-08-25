"""
問題URL: https://atcoder.jp/contests/abc062/tasks/abc062_b
----------------------------------------------------
結果
・4min
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    ans = ["#"*(W+2)]

    for _ in range(H):
        A = input().strip()
        ans.append("#"+A+"#")

    ans.append("#"*(W+2))

    for i in range(len(ans)):
        print(*ans[i], sep="")

if __name__ == "__main__":
    main()