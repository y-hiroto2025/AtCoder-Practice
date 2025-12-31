"""
問題URL: https://atcoder.jp/contests/abc333/tasks/abc333_b
----------------------------------------------------
解法ポイント、学び
・
----------------------------------------------------
"""
def main():
    """vertex = ["A", "B", "C", "D", "E"]"""
    S = input()
    T = input()
    """S_length = abs(vertex.index(S[0]) - vertex.index(S[1]))
    T_length = abs(vertex.index(T[0]) - vertex.index(T[1]))"""

    s1 = ord(S[0]) - ord('A')
    s2 = ord(S[1]) - ord('A')
    S_length = abs(s1 - s2)

    t1 = ord(T[0]) - ord('A')
    t2 = ord(T[1]) - ord('A')
    T_length = abs(t1 - t2)

    if min(S_length, 5 - S_length) == min(T_length, 5 - T_length):
        print("Yes")
    
    else:
        print("No")
   

if __name__ == "__main__":
    main()