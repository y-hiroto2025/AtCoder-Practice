"""
問題URL: https://atcoder.jp/contests/abc182/tasks/abc182_c
----------------------------------------------------
結果
・自力（15min）
----------------------------------------------------
"""
import itertools

def main():
    N = input().strip()
    N_list = [int(i) for i in N]
    k = len(N)

    for i in range(k):
        comb = list(itertools.combinations(N_list, k-i))
        for c in comb:
            if sum(c) % 3 == 0:
                print(i)
                return
    
    print(-1)


if __name__ == "__main__":
    main()