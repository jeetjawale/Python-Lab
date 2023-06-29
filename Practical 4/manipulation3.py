list1=[22.4,4.0,16.22,9.1,5.2,11.0,17.50]
list2=[round(num) for num in list1]
list2.sort()
max1 = max(list2)
min1 = min(list2)
print("maximum element is :",max1)
print("\nminimum element is :",min1)
list3 = []
for i in list2:
    list3.append(i * 5)
print(' '.join(map(str, list3)))








