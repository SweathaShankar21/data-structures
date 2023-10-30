set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
difference_set1 = set1.difference(set2)
print("Difference (set1 - set2):", difference_set1)
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference)
