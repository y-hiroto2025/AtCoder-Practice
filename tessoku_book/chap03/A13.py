# しゃくとり法
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0

    right = 0

    for left in range(N):
        # rightを進められるだけ進める
        # rightがまだ右に行ける かつ 次のペアの差がK以下
        while right < N - 1 and A[right+1] - A[left] <= K:
            right += 1

        ans += right - left

    print(ans)

if __name__ == "__main__":
    main()

"""
import sys
import bisect

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        # A[i] + K 以下の数字が、配列のどこまで入るか？を探す
        # bisect_right は「挿入できる一番右の位置」を返す = その数以下の個数
        limit_pos = bisect.bisect_right(A, A[i] + K)
        
        # limit_pos は「個数」なので、インデックスに直すには -1 する必要があるが、
        # ここでは「自分より右にある個数」を知りたい。
        # limit_pos には「自分(i)を含めた、条件を満たす個数」が入っている。
        # そこから「自分自身より左の分(i + 1個)」を引けば、右側のペア数が求まる。
        
        # もっと単純に：
        # 「自分(i)より後ろ」かつ「limit_posより前」の範囲にある個数
        # limit_pos は「条件を満たす末尾の次のインデックス」
        # i は「現在のインデックス」
        # よって個数は limit_pos - (i + 1)
        # ※ただし limit_pos が i 以下になることはない（A[i]+K >= A[i]なので）
        
        count = limit_pos - (i + 1)
        ans += count

    print(ans)

if __name__ == "__main__":
    main()
"""