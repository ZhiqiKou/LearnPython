import time
# from MyWebServer import HTTPServer

HTML_ROOT_DIR = "./html"

class Application(object):
    """框架的核心部分，通用的框架主体程序"""
    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            # 要访问静态文件
            file_name = path[7:]
            # 打开文件 读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 未找到路由信息， 返回404错误
                status = "404 Not Found"
                hearders = []
                start_response(status, hearders)
                return "Not Found"
            else:
                file_data = file.read()
                file.close()

                status = "200 OK"
                hearders = []
                start_response(status, hearders)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                response_body = handler(env, start_response)
                return response_body
        # 未找到路由信息， 返回404错误
        status = "404 Not Found"
        hearders = []
        start_response(status, hearders)
        return "Not Found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "Hello World"

urls = [
    ("/ctime", show_ctime),
    ("/sayhello", say_hello)
]
app = Application(urls)


# if __name__ == '__main__':
#     urls = [
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello)
#     ]
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()


