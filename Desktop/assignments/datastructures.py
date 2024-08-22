my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('my_list after appending elements', my_list)

my_list = my_list[:1] + [15] + my_list[1:]
print('my_list after appending 15:', my_list)


list2 = [50, 60, 70]
print('list2:', list2)

my_list.extend(list2)
print('my_list after extending list2:', my_list)

del my_list[-1]
print('my_list after deleting lastelement:',  my_list)

my_list.sort()
print('sorted list:', my_list)

index = my_list.index(30)
print('index of 30:', index)

