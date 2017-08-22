class A(object):     # deriving from 'object' declares A as a 'new-style-class'
    def __init__(self):
        self.k = 1


    def foo(self):
        print "foo"

class B(A):
    def __init__(self):
        self.k1 = 11


    def foo(self):
        super(B, self).foo()   # calls 'A.foo()'

myB = B()
myB.foo()






