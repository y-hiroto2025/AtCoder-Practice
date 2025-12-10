# 問題URL: https://atcoder.jp/contests/abc092/tasks/abc092_b


def main():
    n = int(input())
    d, x = map(int, input().split())
    
    for a_i in range(n):
        a_i = int(input())
        m = 0
        while True:
            if (m * a_i) + 1 > d:
                break
            m += 1
        x += m
    return x

def main_class():
    # classを使って書いてみる
    pass

if __name__ == "__main__":
    print(main())
