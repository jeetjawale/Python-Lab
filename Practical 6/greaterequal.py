def extract_tuples_with_three_elements(lst):
    result = []
    for tup in lst:
        if len(tup) >= 3:
            result.append(tup)
    return result


my_list = [(2,3), (1,2),(3, 4, 5), (10,), (5,6,7,8)]
new_list = extract_tuples_with_three_elements(my_list)
print(new_list)
