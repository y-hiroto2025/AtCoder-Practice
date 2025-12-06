# 問題URL: https://atcoder.jp/contests/abc143/tasks/abc143_b

# N個のたこ焼き
# i個目はおいしさd[i]
# おいしさx, yの二つを食べると体力が + x*y
# nC2 = n(n-1)/2
# ２個一緒に食べたときの体力回復量の総和

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