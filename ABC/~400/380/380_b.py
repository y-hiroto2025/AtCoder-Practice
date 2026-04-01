"""
問題URL: https://atcoder.jp/contests/abc380/tasks/abc380_b
----------------------------------------------------
結果
・自力（10min）
----------------------------------------------------
"""
def main():
    N, K = map(int, input().split())
    S = input().strip()

    cnt = 0
    eat = True
    ans = 0

    for i in range(N):
        if S[i] == "O":

            if eat == False:
                cnt = 1
                eat = True
            else:
                cnt += 1

        else:
            eat = False
        
        if cnt == K:
            ans += 1
            cnt = 0
    
    print(ans)


if __name__ == "__main__":
    main()