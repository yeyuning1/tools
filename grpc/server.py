import time
from concurrent.futures import ThreadPoolExecutor
import reco_pb2, reco_pb2_grpc
import grpc

# 1.自定义服务类(继承模板类), 重写远程调用的函数
# 2.实现gRPC服务器

# 自定义服务类
class RecoServicer(reco_pb2_grpc.RecoServicer):
    def article_recommand(self, request, context):
        # 获取数据
        print(request.user_id)
        print(request.channel_id)
        print(request.time_stamp)

        response = reco_pb2.RecoResponseArgs()
        response.pre_time_stamp = 1567149355934
        # 返回一组伪数据
        article_list = []
        for i in range(request.article_num): # range(5) 0-4
            article = reco_pb2.Article()
            article.article_id = i + 1
            article.track.click = 'user:{}:article:{}:click'.format(request.user_id, i + 1)
            article.track.read = 'user:{}:article:{}:read'.format(request.user_id, i + 1)
            article.track.collect = 'user:{}:article:{}:collect'.format(request.user_id, i + 1)
            article_list.append(article)

        response.articles.extend(article_list)
        return response

# 实现服务器
def serve():
    # 1. 创建服务器
    executor = ThreadPoolExecutor(max_workers=10)
    server = grpc.server(executor)
    # 2. 注册远程调用的函数
    reco_pb2_grpc.add_RecoServicer_to_server(RecoServicer(), server)
    # 3. 监听端口号
    server.add_insecure_port('0.0.0.0:8900')
    # 4. 启动服务器  非阻塞
    server.start()
    while True:
        time.sleep(24 * 60 * 60)


if __name__ == '__main__':
    serve()