import itertools

def main():
    S, K = input().split()

    comb = sorted(set(itertools.permutations(S)))
    print("".join(comb[int(K)-1]))


if __name__ == "__main__":
    main()