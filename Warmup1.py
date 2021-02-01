x = 5
y = 2

print("the sum of", x, "and", y, " is", x + y)


'''
This is a multiline comment
it will not be interpreted
good to know
'''

print('my name is', 'Hamza')

age = 20
AGE = 40

print(AGE, age)

x = 'value'
print('e' not in x) # returns false because 'e' is in x

a = 10;
print(a, id(a));    # id(a) returns the memory location/address of a
b = 10;
print(b, id(b));

print(a is b);  # return true because a and b point to the same memory location

'''
for values a, b in the range [-257, 257] inclusive, the operaion "a is b" will return false.
However, outside that range, python asigns pointers to variable for better memory management because numbers become too large
and creating number memory location each time a variable is declared becomes too costly.
'''

a = '1+3j'
print(type(a))  # returns the type of the variable a.

a, b = 1100, 1100
small = a if a < b else b if b < a else 100
print(small)



########
count = 0;
while count < 4:
    print("count", count)
    count += 1
    break       # skips the else block too and execute the last print statement
else:
    print("inside else")

print("DONE!")


while count < 4:
    print("count", count)
    count += 1
    continue       # skips the else block too and execute the last print statement
else:
    print("inside else")

print("DONE!")