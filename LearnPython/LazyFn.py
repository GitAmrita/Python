def lazy(func):
    def lazyfunc(*args, **kwargs):
        wrapped = lambda x : func(*args, **kwargs)
        wrapped.__name__ = "lazy-" + func.__name__
    	return wrapped
	return lazyfunc


def hello_add_normal(x, y):
	print "Hello I am Normal!"
	return x + y


@lazy
def hello_add_lazy(x, y):
	print "Hello I am Lazy!"
	return x + y


myVal = hello_add_lazy(1, 2)
myVal()
