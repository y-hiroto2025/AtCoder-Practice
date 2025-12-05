# 問題URL: https://atcoder.jp/contests/abc092/tasks/arc093_a


def main():
    num = int(input())
    spots = [0] + list(map(int, input().split())) + [0]
    total_money = 0

    for i in range(num + 1):
        total_money = total_money + abs(spots[i] - spots[i+1])
    for i in range(1, num + 1):
        original = abs(spots[i-1] - spots[i]) + abs(spots[i] - spots[i+1])
        shortcut = abs(spots[i-1] - spots[i+1])
        money = total_money - original + shortcut
        print(money)

if __name__ == "__main__":
    main()