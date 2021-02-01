
# DAY THREE HANDS ON ASSIGNMENT

'''
    1. Convers fib series using generators
'''

def fib(n):
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a, b = b, a + b
        count += 1

f = fib(10)
for x in f:
    print(list(f))



'''
    2. Display prime numbers from n1 to n2 using iterators and generators
'''

class Primos:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __iter__(self):
        return self

    def __next__(self):
        val = self.n1

        if self.n1 > self.n2:
            raise StopIteration

        self.n1 += 1

        for x in range(2, val):
            if val % x == 0:
                break
        else:
            return val

p = Primos(1, 10)

list_primes= [v for v in p if v is not None]
print(list_primes)



'''Generator method to get prime numbers from 30 to 200'''

def is_prime(n):
    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

def getPrimes(n1, n2):
    while n1 < n2:
        if is_prime(n1):
            yield n1
        n1 += 1

l = list(getPrimes(30, 200))

print(l)



'''
    3. Write a generator which computes the running average for any given list
    input = [7, 13, 17, 231, 12, 8, 3]
    output = [7.00, 10.00, 12.33, 67.00, 56.00, 48.00, 41.57]
'''

def compute_running_avg():
    total, count, avg = 0.0, 0, None

    while True:
        temp = yield avg
        total += temp
        count += 1
        avg = total / count


running_avg = compute_running_avg()
next(running_avg)
a_list = [7, 13, 17, 231, 12, 8, 3]

for v in a_list:
    result = "sent: {val:3d}, new average: {avg:6.2f}"
    print(result.format(val=v, avg=running_avg.send(v)))

