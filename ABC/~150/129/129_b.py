"""
問題URL: https://atcoder.jp/contests/abc129/tasks/abc129_b
----------------------------------------------------
結果
・自力（30min）
----------------------------------------------------
"""

def main():
    num = int(input())
    weights = list(map(int, input().split()))
    ans = []

    total_weight = sum(weights) # 先に合計を計算しておく
    min_diff = total_weight
    for i in range(1, num - 1):
        # s_1 = sum(weights[:t])
        # s_2 = sum(weights[t:])
        s_1 += weights[i]
        s_2 = total_weight - s_1
        # ans.append(abs(s_1 - s_2))
        ans.append(abs(s_1 - s_2))

        diff = abs(s_1 - s_2)
        if diff < min_diff:
            min_diff = diff

    # print(min(ans))

if __name__ == "__main__":
    main()