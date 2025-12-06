# 問題URL: https://atcoder.jp/contests/abc143/tasks/abc143_c

# N匹のスライム横並び
# 色の情報配列S
# 同色隣接＝＞融合
# 最後に残るのは何匹？

def main():
    slime_amount = int(input())
    slime_colors = input()
    left_slimes = 1
    for i in range(slime_amount - 1):
        if slime_colors[i] != slime_colors[i + 1]:
            left_slimes += 1
    print(left_slimes)

if __name__ == "__main__":
    main()