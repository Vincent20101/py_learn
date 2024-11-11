from concurrent.futures import ThreadPoolExecutor

def say_hello():
    print("Hello")
    # 创建20个线程
executor = ThreadPoolExecutor(20)
for i in range(0,10):
    executor.submit(say_hello())