

'Fisrt Recursion Case'

def factorial (n):

    print(n)    

    if n == 1:
        return 1   

    else:
        return (n * factorial(n-1))
    

n = 5

a = factorial(n)

print(a)
