# 問題URL: https://atcoder.jp/contests/abc143/tasks/abc143_b

def main():
    amount = int(input())
    tastes = list(map(int, input().split()))
    stamina = sum(tastes) ** 2
    for i in range(amount):
        if i == 0:
            difference = tastes[i] * tastes[i]
        else:
            difference = sum(tastes[0:i+1]) * tastes[i]
        stamina -= difference
    return stamina

if __name__ == "__main__":
    print(main())