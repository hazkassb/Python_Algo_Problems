# DATA COLLECTION ASSIGNMENT 1

'''
    1. Write a program that reads a mathematical expression in postfix form from the user,
       evaluates it, and displays its value.
'''

def evalOp(op, alist):
    """Evaluate the current operation"""

    rhs, lhs = alist.pop(), alist.pop()
    result = 0

    if op == '+':
        result = lhs + rhs
    elif op == '*':
        result = lhs * rhs
    elif op == '-':
        result = lhs - rhs
    else:
        result = lhs / rhs

    return result

def isOperator(ch):
    """Determines whether a character is an operator"""

    operators = "+-*/"

    return ch in operators

def evaluate():
    """Evaluates a postfix expression"""

    expression = input("Please enter a postfix expression (use white-space to delimit tokens): \n")
    values = list()

    for token in expression.split(" "):
        if token.isdigit():
            val = int(token)
            values.append(val)
        elif isOperator(token):
            result = evalOp(token, values)
            values.append(result)
        else:
            print('invalid character:', token)
            return

    answer = values.pop()
    if len(values) == 0:
        print("answer = ", answer)
        return
    else:
        print("invalid postfix syntax!")
        return

evaluate()



'''
    2. Write a program that reads integers from the user and stores them in a list. Your
    program should continue reading values until the user enters 0. Then it should
    display all of the values entered by the user (except for the 0) in order from smallest
    to largest, with one value appearing on each line. Use either the sort method or
    the sorted function to sort the list.
'''

def read_and_display():
    alist = list()

    while True:
        x = input("Enter an integer: ")
        if x == '0':
            break

        alist.append(int(x))

    alist.sort()

    for val in alist:
        print(val)

read_and_display()



'''
    3. Create a program that reads integers from the user until a blank line is entered.
    Once all of the integers have been read your program should display all of the
    negative numbers, followed by all of the zeros, followed by all of the positive
    numbers. Within each group the numbers should be displayed in the same order
    that they were entered by the user.
    For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then your
    program should output the values -4, -1, -2, 0, 0, 3, and 1.
    Your program should display each value on its own line.
'''

def reader():
    pos, zeros, negs = list(), list(), list()

    while True:
        x = input("Enter an integer: ")
        if x == "":
            break

        if int(x) < 0:
            negs.append((int(x)))
        if int(x) == 0:
            zeros.append((int(x)))
        if int(x) > 0:
            pos.append(int(x))

    for x in negs:
        print(x)
    for x in zeros:
        print(x)
    for x in pos:
        print(x)

    return

reader()



'''
    4. In this exercise, you will create a program that reads words from the user until the
    user enters a blank line. After the user enters a blank line your program should
    display each word entered by the user exactly once. The words should be
    displayed in the same order that they were entered.
    For example, if the user enters:
    first
    second
    first
    third
    second
    then your program should display:
    first
    second
    third
'''

def displayUnique():
    alist = list()

    while True:
        x = input("Type something: ")

        if x == "":
            break

        if x not in alist:
            alist.append(x)

    for val in alist:
        print(val)

    return

displayUnique()



'''
    5. Implement queue FIFO principle using list and its methods. You can use methods
    of list , use proper methods to follow FIFO principles.
'''

class Queue:
    """FIFO --> First-In First-Out data structure"""
    def __init__(self):
        self.data = []

    def add_(self, val):
        self.data.append(val)
        return

    def pop_(self):
        return self.data.pop(0)

    def peek_(self):
        return self.data[0]

q = Queue()
q.add_(5)
q.add_(6)
q.add_(7)
q.add_(10)
print(q.pop_())
print(q.peek_())



'''
    6. Implement stack LIFO principle using list and its method. You can use methods of
    list like pop, append.to solve this problem.
'''

class Stack:
    """LIFO --> Last-In First-Out data structure"""
    def __init__(self):
        self.data = list()

    def add_(self, val):
        self.data.append(val)

    def pop_(self):
        return self.data.pop()

    def peek_(self):
        return self.data[len(self.data)-1]

st = Stack()
st.add_(12)
st.add_(1)
st.add_(-2)
st.add_(0)
st.add_(-4)
st.add_(6)
print(st.pop_())
print(st.peek_())



'''
    7. Write a Python program that accepts a hyphen-separated sequence of words as
    input and prints the words in a hyphen-separated sequence after sorting them
    alphabetically.
    I/P: ‘We-like-to-work-with-python’
    O/P: ‘We-like-python-to-with-work’
'''

def sort_display():
    seq = input("enter a hyphen-separated sequence of words: ")

    alist = seq.split("-")
    alist.sort()

    res = "-".join(alist)
    print(res)

sort_display()

