"""
問題URL: https://atcoder.jp/contests/abc349/tasks/abc349_b
----------------------------------------------------
結果
・ギブアップ

なぜ解けなかった？
・if文の条件文があまっかった
if i_count != 2 and i_count != 0:

解法ポイント、学び
・collectionsを使えば楽
----------------------------------------------------
"""
import collections
def main():
    S = input()
    s_count = {}

    c = collections.Counter(S)
    count_of_counts = collections.Counter(c.values())
    for num in count_of_counts.values():
        if num != 2 and num != 0:
            print("No")
            return
        print("Yes")

    """for i in range(len(S)):
        if S[i] not in s_count:
            s_count[S[i]] = 1
        else:
            s_count[S[i]] += 1
    print(s_count)
    count_list = list(s_count.values())

    ans = "Yes"

    for i in range(1, max(count_list) + 1):
        i_count = 0

        for num in count_list:
            if num == i:
                i_count += 1
        if i_count != 2:
            ans = "No"
            break    
    print(ans)"""

if __name__ == "__main__":
    main()