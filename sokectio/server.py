# 2.创建socketio服务器
import socketio

# JWT的秘钥
JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
# 消息队列的地址
RABBIT_MQ = 'amqp://guest:guest@192.168.105.128:5672'

# 创建socketio的消息队列的管理器
mgr = socketio.KombuManager(RABBIT_MQ)

# 设置client_manager=队列管理器后, im服务器就可以作为消费者从消息队列中自动取出消息进行发送
sio = socketio.Server(async='eventlet', client_manager=mgr)

# 3.创建sio应用  管理im服务
app = socketio.Middleware(sio)

