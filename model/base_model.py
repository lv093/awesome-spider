from model import db
from utils import logger
from utils.dataHelper import data_helper
import traceback
from utils.time import time_format
import datetime, json,time

"""
    ORM
"""


class BaseModel:
    __unique_attr__ = []

    # 按条件查询第一条数据
    def find(self, cond_dict):
        search = {}
        for k, v in cond_dict.items():
            if not hasattr(self, k):
                logger.info(self.__tablename__ + " orm find 参数有问题 key:" + k)
            else:
                search[k] = v
        if len(search) == 0:
            logger.info("%s search param is null", self.__tablename__)
            return None
        data = self.query.filter_by(**search).first()
        db.session.commit()
        return data

    # 按条件查询所有
    def find_all(self, cond_dict):
        search = {}
        for k, v in cond_dict.items():
            if not hasattr(self, k):
                logger.info(self.__tablename__ + " orm find 参数有问题 key:" + k)
            else:
                search[k] = v
        if len(search) == 0:
            logger.info("%s search param is null", self.__tablename__)
            return None
        data = self.query.filter_by(**search).all()
        db.session.commit()
        return data

    def find_no_commit_all(self, cond_dict):
        """
        按照条件查询所有不执行commit
        """
        search = {}
        for k, v in cond_dict.items():
            if not hasattr(self, k):
                logger.info(self.__tablename__ + " orm find 参数有问题 key:" + k)
            else:
                search[k] = v
        if len(search) == 0:
            logger.info("%s search param is null", self.__tablename__)
            return None
        data = self.query.filter_by(**search).all()
        return data

    @classmethod
    def split_candidates(cls, candidates: dict, size: int):
        result = []
        each = {}
        for k, v in candidates.items():
            each[k] = v
            if len(each) >= size:
                result.append(each)
                each = {}

        if len(each) > 0:
            result.append(each)
        return result


    # 批量同步数据到DB
    def sync_batch(self, attr_dict_list):
        update_list=[]
        index=-1
        try:
            for attr_dict in attr_dict_list:
                index+=1
                orm = self.__class__()
                if len(self.__unique_attr__) == 0:
                    raise NameError(self.__tablename__ + " unique_attr is null")
                search = {}
                for k in self.__unique_attr__:
                    if hasattr(self, k):
                        search[k] = attr_dict[k]
                    else:
                        raise NameError(self.__tablename__ + " orm find 参数有问题 key:" + k)
                # 查询是否存在
                exist = orm.find(search)
                # 创建 or 修改
                if exist is None:
                    # 给orm赋值
                    for k, v in attr_dict.items():
                        if hasattr(orm, k):
                            setattr(orm, k, v)
                    if hasattr(orm, "created_at"):
                        setattr(orm, "created_at", time_format.now_to_date())
                    if hasattr(orm, "updated_at"):
                        setattr(orm, "updated_at", time_format.now_to_date())
                    db.session.add(orm)
                    update_list.append(index)
                else:
                    is_edit = False
                    for k, v in attr_dict.items():
                        if hasattr(exist, k):
                            ov = getattr(exist, k)
                            if isinstance(ov, datetime.datetime) or isinstance(ov, datetime.date) or isinstance(ov,
                                                                                                                datetime.time):
                                ov = str(ov)
                                if ov == v:
                                    continue
                            elif ov == v:
                                continue
                            is_edit = True
                            setattr(exist, k, v)
                    if is_edit:
                        update_list.append(index)
                    if hasattr(orm, "updated_at"):
                        setattr(orm, "updated_at", time_format.now_to_date())
                    # setattr(exist, "updated_at", time_format.now_to_date())
                    db.session.add(exist)
            #logger.info('current pool size :%s %s %s ', db.engine.pool.checkedin(), db.engine.pool.checkedout(),
            #            db.engine.pool.size())
            db.session.commit()
        except Exception as err:
            logger.error('==== orm sync_batch err %s %s ====[%s]', self.__class__.__name__, err, traceback.format_exc())
            db.session.close()
            return []
        return update_list

    # 可一次insert多条数据
    def sync_batch_new(self, attr_dict_list):
        try:
            orm_list = []
            for attr_dict in attr_dict_list:
                orm = self.__class__()
                if len(self.__unique_attr__) == 0:
                    raise NameError(self.__tablename__ + " unique_attr is null")
                search = {}
                for k in self.__unique_attr__:
                    if hasattr(self, k):
                        search[k] = attr_dict[k]
                    else:
                        raise NameError(self.__tablename__ + " orm find 参数有问题 key:" + k)
                # 查询是否存在
                exist = orm.find(search)
                # 创建 or 修改
                if exist is None:
                    # 给orm赋值
                    for k, v in attr_dict.items():
                        if hasattr(orm, k):
                            setattr(orm, k, v)
                    orm_list.append(orm)
                else:
                    for k, v in attr_dict.items():
                        if hasattr(exist, k):
                            setattr(exist, k, v)
                    db.session.add(exist)
            if len(orm_list) > 0:
                db.session.bulk_save_objects(orm_list)
            db.session.commit()
        except Exception as err:
            logger.error('==== orm sync_batch err %s %s ====[%s]', self.__class__.__name__, err,
                         traceback.format_exc())
            db.session.close()

    # 添加方法 支持批量添加没有update
    def insert(self, attr_dict_list):
        try:
            orm_list = []
            for attr_dict in attr_dict_list:
                orm = self.__class__()
                # 给orm赋值
                for k, v in attr_dict.items():
                    if hasattr(orm, k):
                        setattr(orm, k, v)
                orm_list.append(orm)
            if len(orm_list) > 0:
                db.session.bulk_save_objects(orm_list)
            db.session.commit()
        except Exception as err:
            logger.error('==== orm insert err %s %s ====[%s]', self.__class__.__name__, err, traceback.format_exc())
            db.session.close()

    # 删除数据
    def delete_sync(self, cond_dict):
        data = self.find_all(cond_dict)
        for item in data:
            db.session.delete(item)
        db.session.commit()

    def find_exist(self, cond_dict):
        key = self.get_key(cond_dict)
        item = redis_store.get(key)
        if item is not None:
            return bytes.decode(item)
        item = self.find(cond_dict)
        redis_store.setex(key, 10, item)
        return item

    # 获取cache_key
    @staticmethod
    def get_key(param):
        key = ""
        for k, v in param.items():
            key += str(k) + ":" + str(v) + ":"
        return key

    def find_no_commit(self, cond_dict):
        search = {}
        for k, v in cond_dict.items():
            if not hasattr(self, k):
                logger.info(self.__tablename__ + " orm find 参数有问题 key:" + k)
            else:
                search[k] = v
        if len(search) == 0:
            logger.info("%s search param is null", self.__tablename__)
            return None
        data = self.query.filter_by(**search).first()
        return data

    # 可一次insert多条数据
    def sync_batch_one_commit(self, attr_dict_list):
        try:
            orm_list = []
            for attr_dict in attr_dict_list:
                orm = self.__class__()
                if len(self.__unique_attr__) == 0:
                    raise NameError(self.__tablename__ + " unique_attr is null")
                search = {}
                for k in self.__unique_attr__:
                    if hasattr(self, k):
                        search[k] = attr_dict[k]
                    else:
                        raise NameError(self.__tablename__ + " orm find 参数有问题 key:" + k)
                # 查询是否存在
                exist = orm.find_no_commit(search)
                # 创建 or 修改
                if exist is None:
                    # 给orm赋值
                    for k, v in attr_dict.items():
                        if hasattr(orm, k):
                            setattr(orm, k, v)
                    orm_list.append(orm)
                else:
                    for k, v in attr_dict.items():
                        if hasattr(exist, k):
                            setattr(exist, k, v)
                    db.session.add(exist)
            if len(orm_list) > 0:
                db.session.bulk_save_objects(orm_list)
            db.session.commit()
        except Exception as err:
            logger.error('==== orm sync_batch err %s %s ====[%s]', self.__class__.__name__, err,
                         traceback.format_exc())
            db.session.close()

    # 可一次insert多条数据, 存在则不插入
    def sync_insert_one_commit(self, attr_dict_list):
        try:
            orm_list = []
            for attr_dict in attr_dict_list:
                orm = self.__class__()
                if len(self.__unique_attr__) == 0:
                    raise NameError(self.__tablename__ + " unique_attr is null")
                search = {}
                for k in self.__unique_attr__:
                    if hasattr(self, k):
                        search[k] = attr_dict[k]
                    else:
                        raise NameError(self.__tablename__ + " orm find 参数有问题 key:" + k)
                # 查询是否存在
                exist = orm.find_no_commit(search)
                # 创建 or 修改
                if exist is None:
                    # 给orm赋值
                    for k, v in attr_dict.items():
                        if hasattr(orm, k):
                            setattr(orm, k, v)
                    orm_list.append(orm)
                else:
                   continue

            if len(orm_list) > 0:
                db.session.bulk_save_objects(orm_list)
            db.session.commit()
        except Exception as err:
            logger.error('==== orm sync_insert_one_commit err %s %s ====[%s]', self.__class__.__name__, err,
                         traceback.format_exc())
            db.session.close()
            return False
        return True

    # 可一次insert多条数据, 存在则不插入
    def sync_insert(self, attr_dict_list):
        try:
            orm_list = []
            for attr_dict in attr_dict_list:
                orm = self.__class__()
                if len(self.__unique_attr__) == 0:
                    raise NameError(self.__tablename__ + " unique_attr is null")
                search = {}
                for k in self.__unique_attr__:
                    if hasattr(self, k):
                        search[k] = attr_dict[k]
                    else:
                        raise NameError(self.__tablename__ + " orm find 参数有问题 key:" + k)
                # 查询是否存在

                for k, v in attr_dict.items():
                    if hasattr(orm, k):
                        setattr(orm, k, v)
                orm_list.append(orm)

            if len(orm_list) > 0:
                db.session.bulk_save_objects(orm_list)
            db.session.commit()
        except Exception as err:
            logger.error('==== orm sync_insert_one_commit err %s %s ====[%s]', self.__class__.__name__, err,
                         traceback.format_exc())
            db.session.close()
            return False
        return True

