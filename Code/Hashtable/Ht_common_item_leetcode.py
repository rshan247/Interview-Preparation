from collections import defaultdict

def def_value():
    return 0

def item_in_common(list1, list2):
    my_dict = defaultdict(int)
    common_items = []
    for i in list1:
        my_dict[i] += 1
    print(my_dict)
    for j in list2:
        if j not in common_items and j in my_dict:
            common_items.append(j)
    return common_items

list1 = [1,3,5]
list2 = [2,4,5,5]

print(item_in_common(list1, list2))