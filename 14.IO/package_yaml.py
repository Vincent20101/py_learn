# coding:utf-8

import yaml
import json
import sys


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)
    return result


if __name__ == '__main__':
    result = read('muke.yaml')
    print(result, type(result))
    print(dir(yaml))

    data = '{"id":16699347418289799170}'
    parsed = json.loads(data)
    print(parsed['id'])


    # 打印 sys.maxsize
    print(f"sys.maxsize: {sys.maxsize}")

    # 创建一个非常大的整数
    large_number = 10 ** 1000
    print(type(large_number))
    print(f"Large number: {large_number}")

    # 验证 int 的任意精度
    huge_number = 10 ** 10000
    print(type(huge_number))
    print(f"Huge number: {huge_number}")