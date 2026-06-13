"""
問題URL: https://atcoder.jp/contests/abc461/tasks/abc461_c
----------------------------------------------------
結果
・自力（19min）
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    N, K, M = map(int, input().split())

    jewel = []
    for _ in range(N):
        c, v = map(int, input().split())
        jewel.append((c, v))
    
    jewel = sorted(jewel, key=lambda x: x[1], reverse=True)

    idx = 0
    color_cnt = 0
    color_set = set()
    chose_idx_set = set()
    ans = 0

    while color_cnt < M:
        j = jewel[idx]

        if j[0] not in color_set:
            color_set.add(j[0])
            color_cnt += 1
            chose_idx_set.add(idx)
            ans += j[1]
        
        idx += 1
    
    idx = 0

    while color_cnt < K:
        j = jewel[idx]

        if idx not in chose_idx_set:
            ans += j[1]
            color_cnt += 1
        
        idx += 1
    
    print(ans)


if __name__ == "__main__":
    main()