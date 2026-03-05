"""
問題URL: https://atcoder.jp/contests/abc349/tasks/abc349_c
----------------------------------------------------
----------------------------------------------------
"""
def main():
    S = input().strip()
    T = input().strip().lower()

    idx = 0
    for s in S:

        if s == T[idx]:
            idx += 1
        
        if idx == 3:
            break
    
    if idx == 3 or (idx == 2 and T[2] == "x"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()