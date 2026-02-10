# 累積和
def main():
    N = int(input())
    A = list(map(int, input().split())) # i号室の部屋人数
    pfx_r = [A[0]]
    pfx_l = [A[-1]]
    for i in range(1, N):
        pfx_r.append(max(pfx_r[i-1], A[i]))
        pfx_l.append(max(pfx_l[i-1], A[-i - 1]))
    pfx_l = pfx_l[::-1]

    D = int(input())
    for i in range(D):
        L_i, R_i = map(int, input().split()) # i日目はL_i~R_i号室が工事
        max_l = pfx_r[L_i-1 - 1]
        max_r = pfx_l[R_i+1 - 1]
        print(max(max_l, max_r))

if __name__ =="__main__":
    main()