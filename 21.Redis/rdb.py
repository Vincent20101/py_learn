import json, redis

#500G, 特殊 一行
def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)

    if not chunk:
      #说明已经读到了文件结尾
      yield buf
      break
    buf += chunk

# with open("input.txt") as f:
#     for line in myreadlines(f, "{|}"):
#         print (line)
# with open('rdb.json', 'r') as json_file:
#   res = json.loads(json_file.read())

# r = redis.Redis(host='172.0.3.64', port=6379, db=0)
# print(r.keys())
# for key, value in res[0].items():
#     r.set(key, json.dumps(value))

from rdbtools import RdbParser, RdbCallback

class RdbInsertCallback(RdbCallback):
    def set(self, key, value, expiry, ttl, data_type, element_count):
        # 处理数据
        pass

def main():
    source_rdb_file = 'dump.rdb'
    with open(source_rdb_file, 'rb') as f:
        parser = RdbParser(RdbInsertCallback())
        parser.parse(f)

if __name__ == "__main__":
    main()