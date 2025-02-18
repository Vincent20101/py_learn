# coding:utf-8

import os
import time
import random
import asyncio
import gevent


def gevent_a():
    for i in range(5):
        print(i, 'a gevent', os.getpid())
        gevent.sleep(random.random() * 2)
    return 'gevent a result'


def gevent_b():
    for i in range(5):
        print(i, 'b gevent', os.getpid())
        gevent.sleep(random.random() * 2)
    return 'b gevent result'



async def a():
    for i in range(10):
        print(i, 'a', os.getpid())
        await asyncio.sleep(random.random() * 2)
    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b', os.getpid())
        await asyncio.sleep(random.random() * 2)
    return 'b function'


async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result[0], result[1])


if __name__ == '__main__':
    start = time.time()
    # asyncio.run(main())

    g_a = gevent.spawn(gevent_a)
    g_a.run()
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a, g_b]
    result = gevent.joinall(gevent_list,  raise_error=True)
    print(result[0].value)
    print(result[1].value)
    print(time.time() - start)
    print('parent is %s' % os.getpid())

    for i, g in enumerate(gevent_list):
        # 判断每个协程的执行情况
        if g.successful() is False:
            # 出现错误 raise_error=False执行完后获取协程的错误
            print(g.exception)
        else:
            # 获取返回值
            print(g.value)