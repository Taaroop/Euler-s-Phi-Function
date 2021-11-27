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

def graph(start, end, m):
    turtle.speed(0)
    for k in range(start, end+1):
        turtle.penup()
        turtle.goto(-770, -400)
        turtle.setheading(0)
        turtle.forward(k*m)
        turtle.left(90)
        turtle.forward(phi(k)*m)
        turtle.dot()

graph(1, 100000, 2)