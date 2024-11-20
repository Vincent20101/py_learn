import sys
import os
from pprint import pprint

sys.path.append('/root/python_learn/python_demo')
import append_path

pprint(sys.path)
pprint(os.getcwd())

print(append_path.vhost)
print(append_path.say_hello_lhb("lhb"))

