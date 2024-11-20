class Fib(object):
    def __init__(self, num):
        self.res = []
        self.num = num
        a = 0
        b = 1
        for x in range(num):
            self.res.append(a)
            a, b = b, a + b

    def __str__(self):
        return str(self.res)

    def __len__(self):
        return self.num

f = Fib(10)
print(f)
print(len(f))