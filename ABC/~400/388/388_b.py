"""
問題URL: https://atcoder.jp/contests/abc388/tasks/abc388_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, D = map(int, input().split())

    snake = []
    for _ in range(N):
        t, l = map(int, input().split())
        snake.append((t, l))
    
    for k in range(1, D + 1):
        ans = 0
        for i in range(N):
            ans = max(ans, snake[i][0] * (snake[i][1] + k))
        
        print(ans)



if __name__ == "__main__":
    main()