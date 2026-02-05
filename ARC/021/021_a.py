"""
問題URL: https://atcoder.jp/contests/arc021/tasks/arc021_1
----------------------------------------------------
----------------------------------------------------
"""
def main():
    A = [list(map(int, input().split())) for _ in range(4)]

    ans = "GAMEOVER"
    for i in range(4):
        for j in range(3):
            if A[i][j] == A[i][j + 1]:
                ans = "CONTINUE"
    
    for i in range(3):
        for j in range(4):
            if A[i][j] == A[i + 1][j]:
                ans = "CONTINUE"
    print(ans)

if __name__ == "__main__":
    main()