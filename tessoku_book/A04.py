def main():
    N = int(input())
    """
    binary_N = ["0"] * 10
    for i in range(10):
        binary_N[i] = str(N % 2)
        N = N // 2
    binary_N = list(reversed(binary_N))
    print("".join(binary_N))
    """
    print(f"{N:010b}")
    


if __name__ == "__main__":
    main()