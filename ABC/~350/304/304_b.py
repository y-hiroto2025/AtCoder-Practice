"""
問題URL: https://atcoder.jp/contests/abc304/tasks/abc304_b
----------------------------------------------------
結果
・自力（20min）
----------------------------------------------------
"""

def main():
    N_str = input()
    
    if len(N_str) <= 3:
        print(N_str)
    else:
        N_str = N_str[:3] + "0"*(len(N_str) - 3)
        print(N_str)

if __name__ == "__main__":
    main()