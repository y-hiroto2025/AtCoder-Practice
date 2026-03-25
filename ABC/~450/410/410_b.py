"""
問題URL: https://atcoder.jp/contests/abc410/tasks/abc410_b
----------------------------------------------------
結果
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    box = {n: 0 for n in range(1, N+1)}
    ans = []

    for i in range(Q):
        ball = X[i]

        if ball >= 1:
            box[ball] += 1
            ans.append(ball)
        else:
            min_box = min(box.items(), key=lambda x: x[1])
            box[min_box[0]] += 1
            ans.append(min_box[0])
    
    print(*ans)
            



if __name__ == "__main__":
    main()