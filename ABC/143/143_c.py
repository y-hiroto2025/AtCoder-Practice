# 問題URL: https://atcoder.jp/contests/abc143/tasks/abc143_c

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