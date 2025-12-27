"""
問題URL: https://atcoder.jp/contests/abc323/tasks/abc323_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())
    win_count = {key: 0 for key in range(1, N + 1)}

    for i in range(1, N + 1):
        S_i = input()

        for n in range(len(S_i)):
            if S_i[n] == "o":
                win_count[i] += 1

    rank = []
    for player, win in win_count.items():
        # -winにすることで、はじめから勝ち数の多い順に並べておきながらも数字の小さい方が前に来る
        rank.append([-win, player])
    rank.sort()
    ans = [rank[i][1] for i in range(N)]
    print(*ans)
    

if __name__ == "__main__":
    main()