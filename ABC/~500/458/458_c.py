"""
問題URL: https://atcoder.jp/contests/abc458/tasks/abc458_c
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
def main():
    S = input().strip().lower()

    c_coords = []
    c_cnt = 0

    for i in range(len(S)):
        if S[i] == "c":
            c_coords.append(i)
            c_cnt += 1
    
    ans = 0
    for j in range(c_cnt):
        ans += min(c_coords[j], len(S) - c_coords[j] - 1) + 1
    
    print(ans)


if __name__ == "__main__":
    main()