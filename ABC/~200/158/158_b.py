"""
問題URL: https://atcoder.jp/contests/abc158/tasks/abc158_b
----------------------------------------------------
----------------------------------------------------
"""
def main():
    N,A,B = map(int, input().split())

    ans = min(A, N%(A+B)) + A*(N//(A+B))

    print(ans)


if __name__ == "__main__":
    main()