import os
#fork只能用于linux/unix中
pid = os.fork()
print("bobby")
if pid == 0:
  print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
else:
  print('我是父进程：{}.'.format(os.getpid()))
  print('我是子进程：{}.'.format(pid))