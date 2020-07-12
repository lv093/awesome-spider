from .stock.tonghuashun import ths

DEFAULT_BLUEPRINT = (
    ('/stock/ths', ths),
)


# 封装配置蓝本的函数
def init_blueprint(app):
    print("init controller, blueprint")
    # 循环读取元组中的蓝本
    for prefix, blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
