"""
問題URL: https://atcoder.jp/contests/abc419/tasks/abc419_b
----------------------------------------------------
結果
・自力（8min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    Q = int(input())

    ball = {}

    for _ in range(Q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:

            if query[1] in ball:
                ball[query[1]] += 1
            else:
                ball[query[1]] = 1
        
        else:
            for key in sorted(ball.keys()):
                
                if ball[key] >= 1:
                    print(key)
                    ball[key] -= 1
                    break
        



if __name__ == "__main__":
    main()