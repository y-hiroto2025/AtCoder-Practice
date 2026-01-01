import collections

a = collections.Counter("baabcdab")
print(sorted(collections.Counter.most_common(a)))