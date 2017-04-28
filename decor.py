import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)

'''
           fib(3)                                fib(4)
       fib(1)     fib(2)              fib(2)             fib(3)
          1     fib(0) fib(1)    fib(0) fib(1)     fib(1)     fib(2)
                  0      1         0       1         1      fib(0) fib(1)
                                                              0     1
'''



def arg_wrapper( f ):
    def inner( *argv ):
        print '%s: %s' % (f.func_name,argv)
        res = f( *argv )
        return res
    return inner

c = arg_wrapper(fib)
print c(5)



def time_wrapper( f ):
    def inner( *argv ):
        before =  time.time()
        res = f( *argv )
        after = time.time()
        print 'execution time: %f seconds' % (after-before)
        return res
    return inner

c = time_wrapper(fib)
print c(5)
