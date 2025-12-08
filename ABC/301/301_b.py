"""
問題URL: https://atcoder.jp/contests/abc301/tasks/abc301_b
----------------------------------------------------
結果
・ギブアップ（バグる原因がわからなかった）

なぜ解けなかった？
・最初の要素、最後の要素が消えたり、二つになったりした。

解法ポイント、学び
・間を埋める系の問題はルールを統一する
・
----------------------------------------------------
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = []

    for i in range(N-1):
        if A[i] < A[i+1]:
            for j in range(A[i], A[i+1]):
                ans.append(str(j))

        else:
            for j in range(A[i], A[i+1], -1):
                ans.append(str(j))
    
    ans.append(str(A[-1]))
    
    print(" ".join(ans))

if __name__ == "__main__":
    main()