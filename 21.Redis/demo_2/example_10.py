import redis
import random
from redis_db import pool
from concurrent.futures import ThreadPoolExecutor

# 用户id
s = set()
while True:
    if len(s) == 1000:
        break
    num = random.randint(10000, 100000)
    s.add(num)

con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete("kill_total", "kill_num", "kill_flag", "kill_user")
    con.set("kill_total", 50)
    con.set("kill_num", 0)
    con.set("kill_flag", 1)
    con.expire("kill_flag", 600)
except Exception as e:
    print(e)
finally:
    del con

executor = ThreadPoolExecutor(200)


def buy():
    connection = redis.Redis(
        connection_pool=pool
    )
    pipline = connection.pipeline()
    try:
        # 如果抢购有效
        if connection.exists("kill_flag") == 1:
            # 监视成功抢购数，成功抢购的ID
            pipline.watch("kill_num", "kill_user")
            # 商品总数
            total = int(pipline.get("kill_total").decode("utf-8"))
            # 成功抢购数
            num = int(pipline.get("kill_num").decode("utf-8"))
            if num < total:
                pipline.multi()
                pipline.incr("kill_num")
                user_id = s.pop()
                pipline.rpush("kill_user", user_id)
                pipline.execute()
    except Exception as e:
        print(e)
    finally:
        if "pipline" in dir():
            pipline.reset()
        del connection


for i in range(0, 1000):
    executor.submit(buy)

print("秒杀已经结束")
