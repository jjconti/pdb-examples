def fib(n):
    a, b = 0, 1
    while a < n:
        import pdb; pdb.set_trace()
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)