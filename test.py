a = "ACABABCBC"
print("A" in a)
print(type(a.count("A")))

print("A" * a.count("A") + "B" * a.count("B"))
A = "AAABBB"
print(A == "A"*a.count("A") + "B"*a.count("B"))