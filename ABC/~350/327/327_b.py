"""
問題URL: https://atcoder.jp/contests/abc327/tasks/abc327_b
----------------------------------------------------
結果
・自力（13min）
----------------------------------------------------
"""
def main():
    B = int(input())
    for i in range(1, 17):
        if i ** i == B:
            print(i)
            return
        elif i ** i > B:
            print(-1)
            return

if __name__ == "__main__":
    main()