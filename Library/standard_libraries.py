# collections
import collections
S = ["a", "b", "a", "A", "c"]
print("文字数をカウント", collections.Counter(S))
max_count = collections.Counter(S).most_common(1)[0][1]
print("最大文字数", max_count)

# itertools
import itertools



# math
import math



# heapq, bisect, from sys setrecursionlimit