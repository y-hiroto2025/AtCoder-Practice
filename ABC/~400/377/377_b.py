"""
問題URL: https://atcoder.jp/contests/abc378/tasks/abc378_b
----------------------------------------------------
結果
・自力（7min）
----------------------------------------------------
"""
def main():
    S = list(input().strip() for _ in range(8))

    risk_x = set()
    risk_y = set()

    for i in range(8):
        for j in range(8):

            if S[i][j] == "#":
                risk_x.add(i)
                risk_y.add(j)

    ans = 0
    for i in range(8):
        if i in risk_x:
            continue
        
        for j in range(8):
            if j not in risk_y:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()