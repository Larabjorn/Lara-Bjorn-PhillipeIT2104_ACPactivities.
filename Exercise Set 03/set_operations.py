set1 = {8,16,24,32,44}
set2 = {7,14,8,32,21}

print("Set Difference")
difference_set = set1.difference(set2)
difference_set = set2.difference(set1)

print(difference_set)

print("Union of Sets")
union_set = set1.union(set2)

print(union_set)

print("Symmetric Difference")
symdiff_set = set1.symmetric_difference(set2)
symdiff_set = set2.symmetric_difference(set1)

print(symdiff_set)

print("Set Intersection")
intersection_set = set1.intersection(set2)
intersection_set = set2.intersection(set1)

print(intersection_set)