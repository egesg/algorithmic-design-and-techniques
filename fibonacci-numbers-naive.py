def fib_recurs(n):
    if n <= 1:
        return n
    else:
        return fib_recurs(n-1) + fib_recurs(n-2)
    
print(fib_recurs(0))
print(fib_recurs(1))
print(fib_recurs(2))
print(fib_recurs(3))
print(fib_recurs(4))
print(fib_recurs(5))
print(fib_recurs(6))
print(fib_recurs(7))
print(fib_recurs(8))
print(fib_recurs(9))
print(fib_recurs(10))

'''
0
1
1
2
3
5
8
13
21
34
55
'''
# https://www.cs.usfca.edu/~galles/visualization/DPFib.html