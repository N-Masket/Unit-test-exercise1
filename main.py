def factorial(n):
    """Calculates the factorial of a non-negative integer."""

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:      
        return 1    
    else:
        return n * factorial(n - 1)
    
    

def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence."""
    # TODO: Implement the logic
    return None


#Returns a list for the FizzBuzz game up to n.
def fizzbuzz(n):
    result = []
    
    for i in range(1, n+1):   
        if i%5==0 and i%3==0:  # Multiples of both 3 and 5 are "FizzBuzz"
          result.append("FizzBuzz")
        elif i % 3 == 0:               #- Multiples of 3 are "Fizz"
         result.append("Fizz")
        elif i % 5 == 0:
          result.append("Buzz")    # Multiples of 5 are "Buzz"
        else:
          result.append(i)          
    return result
    
   
