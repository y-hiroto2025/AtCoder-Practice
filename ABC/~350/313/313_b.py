"""
問題URL: https://atcoder.jp/contests/abc313/tasks/abc313_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N, M = map(int, input().split())
    losers = set()
    winners = []

    for _ in range(M):
        A_i, B_i = map(int, input().split())
        losers.add(B_i)
    
    for i in range(1, N + 1):
        if i not in losers:
            winners.append(i)

    if len(winners) == 1:
        print(winners[0])
    else:
        print(-1)

if __name__ == "__main__":
    main()