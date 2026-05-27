"""
問題URL: https://atcoder.jp/contests/abc025/tasks/abc025_b
----------------------------------------------------
結果
・自力（9min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())

    curr_coord = 0
    move = {"West": -1, "East": 1}
    
    for _ in range(N):
        s, d = input().split()
        d = int(d)

        if d < A:
            curr_coord += A * move[s]
        elif A <= d <= B:
            curr_coord += d * move[s]
        else:
            curr_coord += B * move[s]

    if curr_coord == 0:
        print(0)
        return
    
    if curr_coord < 0:
        print("West", -curr_coord)
    else:
        print("East", curr_coord)
    
    return



if __name__ == "__main__":
    main()