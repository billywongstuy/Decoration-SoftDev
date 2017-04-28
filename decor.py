import time

def arg_wrapper( f ):
    def inner( *argv ):
        print '%s: %s' % (f.func_name,argv)
        res = f( *argv )
        return res
    return inner

@arg_wrapper
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)

print fib(5)



def time_wrapper( f ):
    def inner( *argv ):
        before =  time.time()
        res = f( *argv )
        after = time.time()
        print 'execution time: %f seconds' % (after-before)
        return res
    return inner

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib2(n-2) + fib2(n-1)

c = time_wrapper(fib2)
print c(5)
