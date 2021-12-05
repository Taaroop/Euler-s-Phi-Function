import turtle

def gcd(a, b):
    if a >= b:
        c = a
    else:
        c = b
    li = []
    for i in range(1, c):
        if a%i == 0 and b%i == 0:
            li.append(i)
    return li[len(li)-1]

def phi(num):
    count = 0
    for j in range(1, num):
        if gcd(j, num) == 1:
            count += 1
    return count

def graph(start, end, scale, dot_size):
    turtle.speed(0)
    for k in range(start, end+1):
        turtle.penup()
        turtle.goto(-770, -400)
        turtle.setheading(0)
        turtle.forward(k*scale)
        turtle.left(90)
        turtle.forward(phi(k)*scale)
        # Helps to recognise phi of primes in blue, even (except 2) with green, and odd composites with black)
        if phi(k) == k-1:
            turtle.dot(dot_size, "blue")
        elif k % 2 == 0:
            turtle.dot(dot_size, "green")
        else:
            turtle.dot(dot_size, "black")
        
        # Analysis
        # It can be seen that the blue (primes) form a straight line on top.
        # This is because phi(prime) = prime - 1. This is the maximum phi function output for any natural number.
        # Also, the black (odd composites) are on top of the green (even numbers).
        # This is because for an even numeber, all the even numbers before it will at least share a factor of 2 with that number. So, half of the numbers cannot be counted in the phi function.
        # From the rest of the numbers, some will be selected, and some will be not. On the other hand, for the odd numbers, the half of the numbers less than that don't necessarily share any factors with that number.
       
        
graph(1, 100000, 2)
