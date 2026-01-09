# 入力した回と問題のフォルダとファイルを作成し、テンプレを書き込む
import os
import sys
from textwrap import dedent
import webbrowser

def main():
    BASE_DIR = r"C:\Users\Y139h\Desktop\Python\AtCoder\ABC"
    while True:
        print(f"\n==== Next Prolem ====")

        # 入力
        try:
            val = input("ABC number (0 to quit): ")
            if val == "0": break
            num = int(val)
            prob = input("problem (a/b/c/...): ").lower()
        except ValueError:
            print("input number !")
            continue

        # フォルダ番号計算
        abc_folder_num = ((num - 1) // 50 + 1) * 50

        # パス作成
        target_folder = os.path.join(BASE_DIR, f"~{abc_folder_num:03}", f"{num:03}")
        file_name = f"{num:03}_{prob}.py"
        full_path = os.path.join(target_folder, file_name)

        # URL作成
        prob_url = f"https://atcoder.jp/contests/abc{num:03}/tasks/abc{num:03}_{prob}"
        
        # フォルダ作成
        os.makedirs(target_folder, exist_ok=True)

        # ファイル作成
        if not os.path.exists(full_path):
            # テンプレ作成
            content = dedent(f'''"""
問題URL: {prob_url}
----------------------------------------------------
結果
・

なぜ解けなかった？
・

解法ポイント、学び
・
----------------------------------------------------
"""
import sys

input = sys.stdin.readline

def main():


if __name__ == "__main__":
    main()''').strip()
            
            # テンプレを書き込む
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created: {file_name}")

        else:
            print(f"Already exists: {file_name}")
    
    print("\n----finished----")


if __name__ == "__main__":
    main()