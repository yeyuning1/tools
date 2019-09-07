import grpc
from test import test_pb2_grpc, test_pb2


def call_remote_func():
    # 1.建立grpc服务器的连接
    channel = grpc.insecure_channel('127.0.0.1:8900')

    # 2.创建客户端助手(用于对函数名/参数打包)
    stub = test_pb2_grpc.TestStub(channel)

    # 3.封装请求参数类型对象
    request = test_pb2.RequestArgs()
    request.age = 30
    request.scores.extend([40, 50, 60])  # 可以使用list的增删改查语法, 不要对列表字段直接赋值 xx = []
    # 4.调用远程函数
    ret = stub.test1(request)
    # 获取返回的数据
    print(ret.name)
    print(ret.info.max_score)


if __name__ == '__main__':
    call_remote_func()