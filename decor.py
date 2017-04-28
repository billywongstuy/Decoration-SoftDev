import time

def arg_wrapper( f ):
    def inner( *argv ):
        print '%s: %s' % (f.func_name,argv)
        return f( *argv )
    return inner

@arg_wrapper
def fib(n):
    if n <= 1:
        return n
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

@time_wrapper
def fib2(n):
    if n <= 1:
        return n
    return fib2(n-2) + fib2(n-1)

c = time_wrapper(fib2)
print c(5)
