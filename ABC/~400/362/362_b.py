"""
問題URL: https://atcoder.jp/contests/abc362/tasks/abc362_b
----------------------------------------------------
結果
・自力（6min）
----------------------------------------------------
"""
def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    dist_AB = (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2
    dist_BC = (B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2
    dist_CA = (C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2

    dists = sorted([dist_AB, dist_BC, dist_CA])

    if dists[2] == dists[0] + dists[1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()