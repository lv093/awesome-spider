from .app import Config

app_config = {}


def init_config(app):
    print("init config")
    app.config.from_object(Config)
    app.config.from_pyfile("config.py")
    app.config.from_pyfile("env.py", silent=True)
    global app_config
    app_config = app.config
