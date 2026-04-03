"""
問題URL: https://atcoder.jp/contests/abc384/tasks/abc384_b
----------------------------------------------------
結果
・自力（15min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    s = []
    for _ in range(H):
        s.append(input().strip())
    
    T = input().strip()

    cood_move = {"U": (-1,0), "D": (1,0), "L": (0,-1), "R": (0,1)}
    house_set = set()

    for t in T:
        x_move, y_move = cood_move[t][0], cood_move[t][1]

        if s[X + x_move][Y + y_move] == ".":
            X += x_move
            Y += y_move
        
        elif s[X + x_move][Y + y_move] == "@":
            X += x_move
            Y += y_move
            house_set.add((X, Y))
    
    print(X+1, Y+1, len(house_set))




if __name__ == "__main__":
    main()