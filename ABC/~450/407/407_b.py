"""
問題URL: https://atcoder.jp/contests/abc407/tasks/abc407_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    X, Y = map(int, input().split())

    xy_set = set()

    for i in range(1, 7):
        for j in range(1, 7):

            if i+j >= X or abs(i-j) >= Y:
                xy_set.add((i, j)) 
    
    print(len(xy_set) / 36)


if __name__ == "__main__":
    main()