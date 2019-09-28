import math

def main():
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))

    result = geron_sq(a,b,c)
    print(result)

def geron_sq(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

main()
