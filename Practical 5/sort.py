# tuple1 = (('a',23),('b',37),('c',11),('d',29))

# # sorted_tup = tuple(sorted(tuple1))
# # print("Sorted tuple :",sorted_tup)
# # list(tuple1).sort()
# # print(tuple1)

# for i in range(len(tuple1)):
#     if tuple[i]== isinstance(i,int):
        
#         sorted_tup = tuple(sorted(tuple1))
# print("Sorted tuple :",sorted_tup)




# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# sorted_tuple = sorted(tuple1, key=lambda x: x[1])

# print(sorted_tuple)










tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

def sort_by_second_item(t):
    return t[1]

sorted_tuple = sorted(tuple1, key=sort_by_second_item)

print(sorted_tuple)