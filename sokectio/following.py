# 需求: 让用户id 和 sid进行绑定
# 1.获取用户id: 传递jwt
# 2.绑定用户身份
from server import sio, JWT_SECRET
from flask import Request


def _get_user_id(token):  # 取出用户id
    # 取出jwt中的数据
    from jwt_util import verify_jwt
    payload = verify_jwt(token, secret=JWT_SECRET)
    if payload:
        return payload.get('user_id')
    else:
        return None

@sio.on('connect')
def on_connect(sid, envrion):
    request = Request(envrion)
    token = request.args.get('token')
    user_id = _get_user_id(token)
    # 用户一连接im服务器, 就让其进入自己的用户id对应的房间  room="2"
    print("进入房间: %s" % user_id)
    sio.enter_room(sid, str(user_id))

@sio.on('disconnect')
def on_disconnect(sid):
    rooms = sio.rooms(sid)
    for room in rooms:  # 断开连接, 离开所有的房间
        sio.leave_room(sid, room)