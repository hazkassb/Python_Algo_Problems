def get_len(s):
    # return len(s)
    l = list(s)
    count = 0
    for i in l:
        count += 1

    return count


print(get_len("hamza"))

'''
1. Write a program to add a key to a dictionary
'''


def add_key(l):
    dict_items = {}

    for row in l:
        dict_items.update({row[0]: row[1]})

    print(dict_items)


add_key([[0, 10], [1, 20], [2, 30]])

'''
2. Write a python program to get the key, value and item
'''


def get_key_val(dict_items):
    print()


# def comp():
#     l = ((1, 2, 3, 4,), (3, 5, 2, 1), (2, 2, 3, 1))
#     res = []
#     for(i in range(len(l)):
#         res.append(sum)
#
# comp()


def sort_(arr):
    if (arr[0] < arr[1] and arr[1] < arr[2]):
        return 0
    elif arr[2] < arr[1] and arr[1] < arr[0]:
        return 2
    else:
        return 0


seq = [2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = seq[3:5:1]

print(seq[::-1])

print(arr)


aList = list()
aList.insert(0, 10)
aList.append(12)
aList.append((-45))
aList.insert(0, -5)
aList.append([9, 4, 7])
# aList.extend([9, 4, 7])
#
# print(aList[-2])
# print(aList)
atuple = tuple();
tup = ("Hamza",  24)
l = [1, 2, 3]
atuple = tuple(l)

# print(list(map(tuple)))
# print(tup)

list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

flat_list = [y for x in list_of_list for y in x]
z = zip(list_of_list, list_s)

# print(list(z))
# print(flat_list)
# print(list_of_list)

x = [1, 2, 3, 4, 5, 6]
y = [9, 8, 7, 6, 5, 4]
sol = [z for z in x if z not in y]
print(sol)


