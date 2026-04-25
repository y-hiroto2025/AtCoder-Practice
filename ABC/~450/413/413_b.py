"""
問題URL: https://atcoder.jp/contests/abc413/tasks/abc413_b
----------------------------------------------------
結果
・自力（3min）
----------------------------------------------------
"""
def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]

    ans_set = set()

    for i in range(N):
        for j in range(N):

            if i != j:
                ans_set.add(S[i] + S[j])

    print(len(ans_set))


if __name__ == "__main__":
    main()