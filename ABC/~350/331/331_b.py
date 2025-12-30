"""
問題URL: https://atcoder.jp/contests/abc331/tasks/abc331_b
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""
def main():
    N, S, M, L = map(int, input().split())
    ans = []

    for s in range(20):
        s_egg = 6 * s

        for m in range(20):
            m_egg = 8 * m

            for l in range(20):
                l_egg = 12 * l

                egg_count = s_egg + m_egg + l_egg
                if egg_count >= N:
                    ans.append(s*S + m*M + l*L)

    print(min(ans))


if __name__ == "__main__":
    main()