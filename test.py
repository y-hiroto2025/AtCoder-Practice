from collections import Counter
S = ["a", "b", "a", "A", "c"]

max_count = Counter(S).most_common(1)
print(max_count)