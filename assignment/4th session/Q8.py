def sparce_make(vector : list):
    vector_dict = dict()
    for idx, comp in zip(range(len(vector)), vector):
        if comp != 0:
            vector_dict[idx] = comp
    return vector_dict

# A
def sparce_add(v1 : dict, v2 : dict):
    v1_keys = set(v1.keys())
    v2_keys = set(v2.keys())
    inter_keys = v1_keys.intersection(v2_keys)

    v12 = dict()
    for key in inter_keys:
        v12[key] = v1[key] + v2[key]
    for key in v1_keys - inter_keys:
        v12[key] = v1[key]
    for key in v2_keys - inter_keys:
        v12[key] = v2[key]
    
    return v12

# B
def sparce_dot(v1 : dict, v2 : dict):
    v1_keys = set(v1.keys())
    v2_keys = set(v2.keys())
    inter_keys = v1_keys.intersection(v2_keys)

    sum = 0
    for key in inter_keys:
        sum += v1[key] * v2[key]
    
    return sum

v1 = sparce_make([1, 2, 3])
v2 = sparce_make([4, 5, 6])

print(sparce_add(v1, v2))
print(sparce_dot(v1, v2))