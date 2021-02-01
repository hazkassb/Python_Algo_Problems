# FIRST SET OF HANDS ON EXERCISES

'''
    1. Write a Python program to sum all the items in a list.
'''
def sum_up(alist):
    # sum_ = sum(alist)
    sum_ = 0
    for x in alist:
        sum_ += x

    print(sum_)

sum_up([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



'''
    2. Write a Python program to get the largest and smallest number from a list.
'''
def max_min(alist):
    # print('largest:', max(alist), '; smalles:', min(alist))
    max_, min_ = alist[0], alist[0]

    for x in alist:
        if x > max_:
            max_ = x
        if x < min_:
            min_ = x

    print('largest:', max_, '\nsmalles:', min_)

max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



'''
    3. Write a Python program to generate and print a list of first and last 5
    elements where the values are square of numbers between 1 and 30
    (both included).
'''
def first_last(start, end):
    alist = [x ** 2 for x in range(start, end + 1)]
    print(alist)

    first_five, last_five = alist[0:5:1], alist[25::]

    print('first five:', first_five, '\nlast five:', last_five)

first_last(1, 30)



'''
    4.Write a Python program to find the length of a tuple.
'''
def length(atuple):
    count = 0
    for x in atuple:
        count += 1

    return count

print(length((1, 3, 4, 5, '234', 9)))



'''
    5. Write a Python program convert a given string list to a tuple.
    I/P: python 3.0<class 'str'>
    Convert the input to a tuple: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')<class 'tuple'>
'''
def convert(s):
    arr = list(s)
    atuple = tuple(arr)
    print(atuple)

convert("python")




# SECOND SET OF HANDS ON EXERCISES
'''
    1. Write a Python script to add a key to a dictionary. I/P: {0: 10, 1: 20}
    O/P : {0: 10, 1: 20, 2: 30}
'''
def addkey(adict, k, v):
    adict.update({k: v})

    return adict

print(addkey({0: 10, 1: 20}, 2, 30))



'''
    2. Write a Python program to get the key, value and item in a dictionary.
'''
def get_k_v_item(adict):
    itms = adict.popitem()
    key = itms[0]
    val = itms[1]

    print('key: ', key, '\nvalue:', val, '\nitem:', itms)

get_k_v_item({0: 10, 1: 20, 2: 30, 3: 40, 4: 50})



'''
    3. Write a Python program to drop empty Items from a given Dictionary. 
    I/P: {'c1': 'Red', 'c2': 'Green', 'c3': None}
    O/P : {'c1': 'Red', 'c2': 'Green'}
'''
def drop_empty(adict):
    new_dict = {}
    for (k, v) in adict.items():
        if v is not None:
            new_dict.update({k: v})

    print(new_dict)

drop_empty({"c1": "Red", "c2": "Green", "c3": None})



'''
    4. Write a Python program to remove an item from a set if it is present
    in the set. I/P : {0, 1, 2, 3, 4, 5}, Remove # :4 O/P: {0, 1, 2, 3, 5}
'''
def remove_item(aset, val):
    aset.discard(val)
    print(aset)

remove_item({0, 1, 2, 3, 4, 5}, 4)



'''
    5. Write a Python program to check if two given sets have no elements in common.
'''
def intersect(set1, set2):
    return len(set1.intersection(set2)) == 0

print(intersect({1, 2, 3, 4, 5}, {-3, -4, -5, 6, 7}))



# THIRD SET OF HANDS ON EXERCISES
'''
    1. Write a Python program to compute element-wise sum of given
    tuples. I/P:
        (1, 2, 3, 4)
        (3, 5, 2, 1)
        (2, 2, 3, 1)
        O/P : (6, 9, 8, 6)
'''
x = (1,2,3,4)
y = (3,5,2,1)
z = (2,2,3,1)
res = tuple(map(sum, zip(x, y, z)))
print(res)



'''
    2. Write a Python program to insert a given string at the beginning of
    all items in a list. I/P : [1,2,3,4], string : emp
    O/P : ['emp1', 'emp2', 'emp3', 'emp4']
'''
def insert_(alist, s):
    res = list(s + str(x) for x in alist)
    print(res)

insert_([1, 2, 3, 4], 'emp')



'''
    3. Write a Python program to create a list of empty dictionaries.
    I/P: 5 O/P: [ {}, {}, {}, {}, {} ]
'''
def create_empty_dict(n):
    res = list({} for i in range(n))
    print(res)

create_empty_dict(5)



# FOURTH SET OF HANDS ON EXERCISES

'''
    1. Write a Python function that accepts a string and calculate the
    number of upper case letters and lower case letters.
    I/P : 'The quick Brow Fox‘
    O/P : Upper case characters : 3, Lower case Characters : 12
'''
def counter(s):
    count_up, count_low = 0, 0
    for ch in s:
        if ch.isupper():
            count_up += 1

        if(ch.islower()):
            count_low += 1

    print('Upper case characters:', count_up, ', Lower case characters:', count_low)

counter('The quick Brow Fox')



'''
    2. Write a Python function that takes a list and returns a new list with
    unique elements of the first list. I/P : [1,2,3,3,3,3,4,5]
    O/P : [1, 2, 3, 4, 5]
'''
def removeDuplicated(alist):
    aset = set(alist)
    return list(aset)

print(removeDuplicated([1,2,3,3,3,3,4,5]))



'''
    3. Write a Python function to multiply all the numbers in a list.
    I/P: (8, 2, 3, -1, 7) 
    O/P : -336
'''
def mult(alist):
    prod = 1;
    for x in alist:
        prod *= x

    print(prod)

mult([8, 2, 3, -1, 7])

