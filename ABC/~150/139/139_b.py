"""
問題URL: https://atcoder.jp/contests/abc139/tasks/abc139_b
----------------------------------------------------
結果
・ギブアップ
----------------------------------------------------
"""
def main():
    A, B = map(int, input().split())
    socket = 1
    ans = 0
    while socket < B:
        socket += -1 + A
        ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()