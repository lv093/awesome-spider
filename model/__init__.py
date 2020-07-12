from flask_sqlalchemy import SQLAlchemy
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.jobstores.memory import MemoryJobStore
db = SQLAlchemy()


def init_db(app):
    print("init db")

    stock_data = get_db_uri(
        app.config['DB_STOCK_DATA_HOST'],
        app.config['DB_STOCK_DATA_PORT'],
        app.config['DB_STOCK_DATA_USER'],
        app.config['DB_STOCK_DATA_PWD'],
        app.config['DB_STOCK_DATA_DB'],
    )
    print("init db, stock_data, " + stock_data)

    app.config['SQLALCHEMY_DATABASE_URI'] = stock_data
    app.config['SQLALCHEMY_BINDS'] = {
        'stock_data': stock_data,
    }

    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 600
    app.config['SQLALCHEMY_POOL_SIZE'] = 300
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

def get_db_uri(host, port, user, pwd, db):
    uri = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset=utf8"
    return uri.format(host=host, port=port, user=user, pwd=pwd, db=db)
