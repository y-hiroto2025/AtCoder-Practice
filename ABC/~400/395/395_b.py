"""
問題URL: https://atcoder.jp/contests/abc395/tasks/abc395_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N = int(input())

    ans = [["?"]*N for _ in range(N)]
    white = False

    for i in range(N):
        j = N - i-1

        if i <= j:
            if (i+1) % 2 == 0:
                white = True
            else:
                white = False

        for y in range(i, j+1):
            for x in range(i, j+1):
                if white:
                    ans[y][x] = "."
                else:
                    ans[y][x] = "#"
    
    for s in ans:
        print(*s, sep="")
    
    

if __name__ == "__main__":
    main()