# 协程: 微线程  允许在同一个线程中切换不同的任务
# 主要针对IO密集型的任务(文件读写, 网络数据交互等), 当进行IO操作时, 可以切换到其他任务上, 让CPU继续工作, 提高CPU的利用率

# 1.打补丁  会将所有默认的IO操作进行重写, 将IO操作全部变为异步处理
from eventlet import monkey_patch
monkey_patch()

from server import app
import chat, following
import sys

if len(sys.argv) <= 1:
    print("Usage: python main.py [port]")
    exit(1)

port = int(sys.argv[1])

# 4.监听端口
import eventlet
socket = eventlet.listen(('', port))

# 5.启动服务器
import eventlet.wsgi
eventlet.wsgi.server(socket, app)


