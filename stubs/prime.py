
"""
Prime : 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

"""

#import sympy

#local implementation
def is_prime2(num):
    divs_list = []

    for n in range(1, num + 1):
        if num%n == 0:
            divs_list.append(n)

    if num == 1:
        print("number needs to be greater than 1")
    elif len(divs_list) == 2:
        print("%d is prime" % (num))
    else:
        print("%d is not prime" % (num))


# local implementation
def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

for i in range (1, 100):
    print ('%d is prime: %s' % (i, is_prime(i)))

for i in range (1, 100):
    is_prime2(i)




# print (sympy.isprime(5))
#
# # Output : [2, 3, 5, 7, 11, 13, 17, 19, 23,
# # 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
# # 73, 79, 83, 89, 97]
# print (list(sympy.primerange(0, 100)))
#
# print (sympy.randprime(0, 100))  # Output : 83
# print (sympy.randprime(0, 100))  # Output : 41
# print (sympy.prime(3)) # Output : 5
#print (sympy.prevprime(50)) # Output : 47
#print (sympy.nextprime(50)) # Output : 53
# Output : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
# 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
# 79, 83, 89, 97]
#print (list(sympy.sieve.primerange(0, 100)))