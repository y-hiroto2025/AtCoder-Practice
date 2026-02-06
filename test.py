a = [1, 2, 3, 4, 5, 6]
from collections import deque
k = 1
d = deque(a)
d.rotate(-k)  # 左に k 個ズレる (計算量は O(k) なのでスライスよりマシ)
print(d[1])