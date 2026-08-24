"""
問題URL: https://atcoder.jp/contests/abc124/tasks/abc124_c
----------------------------------------------------
結果
・5min
----------------------------------------------------
"""
def main():
    S = input().strip()

    cost1 , cost2 = 0 , 0

    for i in range(len(S)):
        if i%2 == 0 and S[i] != "0":
            cost1 += 1
        elif i%2 == 1 and S[i] != "1":
            cost1 += 1

        if i%2 == 0 and S[i] != "1":
            cost2 += 1
        elif i%2 == 1 and S[i] != "0":
            cost2 += 1

    print(min(cost1, cost2))


if __name__ == "__main__":
    main()