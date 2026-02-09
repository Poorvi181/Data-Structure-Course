#Fibonacci series

def fibonacci(n):
    if n==0 or n==1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(7):
    print(fibonacci(i))


# factorial using recursion

def factorial(n):
    if n==1:
        print("Reached Base Case.")
        return 1
    
    else:
        print("calling factorial (", n-1, ")")
        return n  factorial(n-1)

print(factorial(7))

#Sum of numbers till n using recursion

def sumofnumbers(n):
    print("Calling of sumofnumbers(",n,")")

    if n==0 or n==1:
        print("Base case reached with n= ", n)")
        return n
    else:
        result= n + sumofnumbers(n-1)
        print("Returning", result, "for n= ", n)
        return result
    
print("Final Answer: ", sumofnumbers(7))

#Power Function

def power(x,y):
    print("calling power(", x,",",y,")")
    
    if y==1:
        print("Base case reached")
        return x
    else:
        half = power(x, y // 2)

        if y%2==0:
            result = half + half
            print("Returning", result, "for power(",x,",",y,")")
            return result
        
        else:
            result = x *half*half
            print("Returning", result, "for power(",x,",",y,")")
            return result
("Final Answer: ", power(3,5))