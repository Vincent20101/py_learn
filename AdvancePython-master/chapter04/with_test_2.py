#!encoding:utf-8
class echo:
    def output(self):
        print('hello world')
    def __enter__(self):
        print('enter')
        return self #返回自身实例，当然也可以返回任何希望返回的东西
    def __exit__(self, exception_type, exception_value, exception_traceback):
        #若发生异常，会在这里捕捉到，可以进行异常处理
        print('exit')
        print(exception_value)
        #如果改__exit__可以处理改异常则通过返回True告知该异常不必传播，否则返回False
        if exception_type == ValueError :
              return True
        else:
              return False
with echo() as e:
  e.output()
  print('do something inside')
print('-----------')
with echo() as e:
  raise ValueError('value error')
print('-----------')
# with echo() as e:
#   raise Exception('can not detect')



from contextlib import contextmanager
# from contextlib import nested
from contextlib import closing
@contextmanager
def make_context(name) :
  print('enter', name)
  yield name
  print('exit', name)
# with nested(make_context('A'), make_context('B')) as (a, b) :
#   print(a)
#   print(b)
with make_context('A') as a, make_context('B') as b :
  print(a)
  print(b)
class Door(object) :
  def open(self) :
    print('Door is opened')
  def close(self) :
    print('Door is closed')
with closing(Door()) as door :
  door.open()


# 使用 ExitStack 代替 nested
from contextlib import ExitStack

# 示例上下文管理器
class CM1:
    def __enter__(self):
        print("Entering CM1")
        return "CM1"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting CM1")

class CM2:
    def __enter__(self):
        print("Entering CM2")
        return "CM2"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting CM2")

# 使用 ExitStack 管理多个上下文
with ExitStack() as stack:
    cm1 = stack.enter_context(CM1())
    cm2 = stack.enter_context(CM2())
    print(f"Using {cm1} and {cm2}")

# 输出：
# Entering CM1
# Entering CM2
# Using CM1 and CM2
# Exiting CM2
# Exiting CM1