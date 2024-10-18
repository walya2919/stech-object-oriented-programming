def remove_neg(num_list : list):
    neg_list = list()
    for item in num_list:
        if item < 0:
            neg_list.append(item)
    
    for neg in neg_list:
        num_list.remove(neg)
    
    return num_list

print(remove_neg([1, 2, 3, -3, 6, -1, -3, 1]))