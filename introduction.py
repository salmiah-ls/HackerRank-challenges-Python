# This code is done on Python 3.

# Challenge 1: Say "Hello, World!" With Python
# https://www.hackerrank.com/challenges/py-hello-world/problem

if __name__ == '__main__':
    print("Hello, World!")

	
# Challenge 2: Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem

f __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n%2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n%2 == 0 and n > 20:
        print("Not Weird")

		
# Challenge 3: Arithmetic Operators
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)	
	
	
# Challenge 4: Python: Division
# https://www.hackerrank.com/challenges/python-division/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

	
# Challenge 5: Loops
# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n:
        print(i*i)
        if i == n:
            break
        i += 1