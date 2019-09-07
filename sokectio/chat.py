from server import sio


@sio.on('chat')
def on_chat(sid, data):
    print("接收到前端发来的数据:%s" % data)
    # TODO 通过gprc将消息内容发送给AI聊天系统
    response = 'AI回复: 请稍等..'
    # 发消息给对应的客户端
    sio.emit('chat', response, room=sid)