"""
問題URL: https://atcoder.jp/contests/abc185/tasks/abc185_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・条件の詰めが甘い。バッテリー容量を超えないこと、途中で0になった時のことを考えていなかった

解法ポイント、学び
・数値が動的な変数で、最大が決まっているなら、超えないようにしないといけない（min(...)）
・入力行数が決まっているならwhileでなくforを使う
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():
    battery, cafe_num, last_time = map(int, input().split())
    current_battery = battery
    current_time = 0

    for _ in range(cafe_num):
        start_time, end_time = map(int, input().split())

        current_battery -= (start_time - current_time)
        if current_battery <= 0:
            print("No")
            break
        
        # 最大容量を超えないようにする
        current_battery += min(battery, end_time - start_time)
    
    current_battery -= (last_time - current_time)

    if current_battery <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()