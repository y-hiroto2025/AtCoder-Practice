"""
問題URL: https://atcoder.jp/contests/abc348/tasks/abc348_b
----------------------------------------------------
結果
・自力（13min）
----------------------------------------------------
"""
def main():
    N = int(input())
    coord = []
    for _ in range(N):
        coord.append(list(map(int, input().split())))

    for i in range(N):
        max_dist = -1
        ans_index = -1

        for j in range(N):
            if i == j:
                continue

            dist = (coord[i][0]-coord[j][0]) ** 2 + (coord[i][1]-coord[j][1]) ** 2

            if dist > max_dist:
                max_dist = dist
                ans_index = j + 1

        print(ans_index)

if __name__ == "__main__":
    main()