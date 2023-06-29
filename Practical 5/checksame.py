# tuple1=(45,45,45,45)

# for i in range(len(tuple1)):
#     if tuple1[0]==tuple1[1]==tuple1[2]==tuple1[3]:
#         pass
        
# print(True)


tuple1=(45,45,45,45)
first_ele=tuple1[0]
for element in tuple1:
    if first_ele !=element:
        result=False
        break
    else:
        result=True

print(result)