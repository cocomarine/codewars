# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod you will return
# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod.

# Solution after learning generators
def productFib(prod):
	a, b = 0, 1

	while prod > a * b:
		a, b = b, a + b

	return [a, b, prod == a * b]



# Solution before learning generators
def productFib(prod):

    current_num = 0
    x = 0

    # while loop going through fibonacci numbers
    while current_num <= prod:
        current_num = fibo(x)
        # if statement for testing True condition
        if prod == fibo(x) * fibo(x+1):
            return [fibo(x), fibo(x+1), True]
        else:
            # for testing False condition
            if prod > fibo(x) * fibo(x+1) and prod < fibo(x+1) * fibo(x+2):
                return [fibo(x+1), fibo(x+2), False]
        # for neither True nor False conditions, increase x by 1
        # so that next fibonacci, fibo(x), can be tested
        x += 1

# function generating fibonacci number
def fibo(n):
    counter = 0
    first = 0
    second = 1
    temp = 0

    while counter < n:
        # temp storing sum of previous fibonacci pairs
        temp = first + second
        # previous second fibo number stored as new first fibo number
        first = second
        # sum of previous fibo pairs stored as new second fibo number
        second = temp
        counter = counter + 1

    return first

