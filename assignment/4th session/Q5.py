ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)

# A
ids.remove(3382)
print(ids)

# B
idx = ids.index(9362)
print(ids)

# C
ids.insert(idx + 1, 4499)
print(ids)

# D
ids = ids + [5566, 1830]
print(ids)

# E
ids.reverse()
print(ids)