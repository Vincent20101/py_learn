class A(object):
    def __init__(self, a):
        print("A")
        print ('init A...')
        self.a = a

class B(A):
    def __init__(self, a):
        print("B")
        super(B, self).__init__(a)
        print ('init B...')

class C(A):
    def __init__(self, a):
        print("C")
        super(C, self).__init__(a)
        print ('init C...')

class D(B, C):
    def __init__(self, a):
        print("D")
        super(D, self).__init__(a)
        print ('init D...')

if __name__ == '__main__':
    d = D("test")