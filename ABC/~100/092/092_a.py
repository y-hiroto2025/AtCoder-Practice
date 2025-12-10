# 問題URL: https://atcoder.jp/contests/abc092/tasks/abc092_a


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    ans = min([a, b]) + min([c, d])

    return ans

def main_class():
    # classを使って書いてみる
    pass

if __name__ == "__main__":
    print(main())