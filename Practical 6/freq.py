from collections import Counter
list = (1,2,1,2,2,3,3,3,3,4)

result = sorted(list, key = list.count )

print(str(result))
    