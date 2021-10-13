#Exercise #4

#the tenth Fibonacci number is Fib(10) = 55. The sum of its digits is 5+5 or 10 and that is also the index number of 55 
# (10-th in the list of Fibonacci numbers)


#Write a recursion function to perform the fibonacci sequence up to the number passed in.

#    Output for fib(5) => 
#    Iteration 0: 1
#   Iteration 1: 1
#    Iteration 2: 2
#    Iteration 3: 3
#    Iteration 4: 5
#    Iteration 5: 8

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
for i in range(15):
    print(fibonacci(i))