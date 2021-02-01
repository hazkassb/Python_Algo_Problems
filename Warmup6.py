from random import randint

'''
1. Make sure you know how to install all these:
        - Install python 2.x/3.x .
        - Install Pycharm IDE or any other IDE
        - Install pip.
        - Update pip using command.
        - Add python interpreter to Pycharm
        - Install jupyter notebook.
'''



'''
2. Write a script which can ceil and floor given value without using any python built-in functions.
'''

def ceil_(val):
    return int(-1 * val // 1 * -1)


def floor_(val):
    return int(val // 1)


print(ceil_(2.3))
print(floor_(-12.9))



'''
3. Python script to swap two integers in single line. [don’t use any python built in function]
'''

def swap_(x, y):
    x, y = y, x
    print("x =", x, ", y =", y)


swap_(3, 6)



'''
4. Write a program that asks the user their name, if they enter your name say "That is a nice name", 
    if they enter "John Cleese" or "Michael Palin", tell them how you feel about them ;), 
    otherwise tell them "You have a nice name."[Use ternary operator].
'''

def great_():
    name = input("What is your name?" + "\n")
    response = "That is a nice name" if name == "Hamza Kassomou" else "let's hang out" if name == "John Cleese" or name == "Michael Palin" else "You have a nice name"
    print(response)


great_()



'''
5. A particular retailer is having a 60 percent off sale on a variety of discontinued products. 
    The retailer would like to help its customers determine the reduced price of the merchandise by having a 
    printed discount table on the shelf that shows the original prices and the prices after the discount has been applied.
    Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new 
    price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure that the discount amounts and the new prices are 
    rounded to 2 decimal places when they are displayed.
'''

def printPrices():
    prices = [4.95, 9.95, 14.95, 19.95, 24.95]
    discounts = []
    new_prices = []

    for price in prices:
        discount = round(0.6 * price, 2)
        new_price = round(price - discount, 2)
        discounts.append(discount)
        new_prices.append(new_price)

    diff = len("discount_amount")
    prices = [' ' * (diff - len("original_price")) + "original_price:"] + prices
    discounts = [' ' * (diff - len("discount_amount")) + "discount_amount:"] + discounts
    new_prices = [' ' * (diff - len("new_price")) + "new_price:"] + new_prices
    # print(*headers)

    table = [prices, discounts, new_prices]
    for row in table:
        for val in row:
            print(val, end='  ')
        print()

printPrices()



'''
6. (Print a table) Write a program that displays the following table: [ do not use ** operator or any 
    python built in function] a b pow(a, b)
    1 2 1
    2 3 8
    3 4 81
    4 5 1024
    5 6 15625
'''

def print_table():
    def pow_(a, b):
        res = 1
        for i in range(b):
            res *= a
        return res

    for i in range(1, 6):
        print(i, i + 1, pow_(i, i + 1))

print_table()



'''
7. (Game: lottery) generate a lottery of a three digit number. The program prompts the user to enter a three-digit 
    number and determines whether the user wins according to the following rules:
        - If the user input matches the lottery number in the exact order, the award is $10,000.
        - If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
        - If one digit in the user input matches a digit in the lottery number, the award is $1,000.
'''

def lotter_game():
    user_input = input("Enter a 3 digit number: ")
    random_ = 982

    print("Today's lucky number is: ", random_)

    def is_match(num1, num2):
        dict = {}

        for ch in str(num1):
            if dict.get(ch) is not None:
                dict.update({ch: 1 + dict.get(ch)})
            else:
                dict.update({ch: 1})

        for ch in str(num2):
            if dict.get(ch) is not None:
                dict.update({ch: dict.get(ch) - 1})
            else:
                dict.update({ch: 1})
        for val in dict.values():
            if val != 0:
                return False

        return True

    user_digit1, user_digit2, user_digit3 = str(user_input)[0], str(user_input)[1], str(user_input)[2]
    if user_input == str(random_):
        print("Congrats! you won $10,000")
    elif is_match(random_, user_input):
        print("Congrats! you won $3000")
    elif user_digit1 in str(random_) or user_digit2 in str(random_) or user_digit3 in str(random_):
        print("Congrats! you won $1000")
    else:
        print("Sadly, you did win anything. Try again!")

lotter_game()



'''
8. (Occurrence of max numbers) Write a program that reads integers, finds the largest of them, and counts its 
    occurrences. Assume that the input ends with number 0. Suppose that you entered 3 5 2 5 5 5 0; the program finds 
    that the largest is 5 and the occurrence count for 5 is 4.
    Enter numbers:
    The largest number is 5
    The occurrence count of the largest number is 4
    3 5 2 5 5 5 0
'''


def find_max():
    sequence = input("Enter a sequence of numbers: ")

    arr = sequence.split()
    curr_max, count, i = 0, 0, 0

    while int(arr[i]) != 0:
        if int(arr[i]) > curr_max:
            curr_max = int(arr[i])
            count = 1
        elif int(arr[i]) == curr_max:
            count += 1
        i += 1

    print("The largest number is", curr_max, "and it occurs", count, "times.")

find_max()



'''
9. write a program to display the following series
        *
       * *
      * * *
     * * * *
    * * * * *
'''

def printTree():
    z = 4
    x = 1
    for i in range(5):
        print(' ' * (5 - (i + 1)), '*' * (2 * i + 1))

printTree()



'''
10. write a program to display the following series
        1 2 3 4 5 6 7
         2 3 4 5 6 7
          3 4 5 6 7
           4 5 6 7
            5 6 7
             6 7
              7
             6 7
            5 6 7
           4 5 6 7
          3 4 5 6 7
         2 3 4 5 6 7
        1 2 3 4 5 6 7

'''

def pattern():
    for i in range(1, 7 + 1):

        for k in range(1, i):
            print(" ", end="")

        for j in range(i, 7 + 1):
            print(j, end=" ")

        print()

    for i in range(7 - 1, 0, -1):

        for k in range(1, i):
            print(" ", end="")

        for j in range(i, 7 + 1):
            print(j, end=" ")

        print()

pattern()



'''
11. (Phone keypads) The international standard letter/number mapping found on the telephone is:
    1 2 3
    ABC DEF
    4 5 6
    GHI JKL MNO
    7 8 9
    PQRS TUV WXYZ
    A program that prompts the user to enter a phone number as a string. The input number may
    contain letters. The program translates a letter (upper- or lowercase) to a digit and leaves all other
    characters intact. Here is a sample run of the program:
    Enter a string: 1-800-Flowers
    1-800-3569377
'''


def toString():
    usr_input = input("Enter sequence: ")

    dict = {}

    dict.update({2: "abc"})
    dict.update({3: "def"})
    dict.update({4: "ghi"})
    dict.update({5: "jkl"})
    dict.update({6: "mno"})
    dict.update({7: "pqrs"})
    dict.update({8: "tuv"})
    dict.update({9: "wxyz"})

    arr = list(usr_input)
    ans = ""

    for i in range(len(arr)):
        if arr[i].isalpha():
            for key in dict.keys():
                if arr[i].lower() in dict.get(key):
                    ans += str(key)
                    continue
        else:
            ans += arr[i]

    print(ans)

toString()
