"""
問題URL: https://atcoder.jp/contests/abc303/tasks/abc303_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    num_people, num_photo = map(int, input().split())
    photos = [list(map(int, input().split())) for _ in range(num_photo)]
    conbination = [[False]*(num_people+1) for _ in range(num_people + 1)]
    ans = 0
    
    for row in photos:
        for i in range(num_people - 1):    
            conbination[row[i]][row[i+1]] = True
            conbination[row[i+1]][row[i]] = True

    for i in range(1, num_people + 1):
        for j in range(i+1, num_people + 1):
            if conbination[i][j] == False:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()