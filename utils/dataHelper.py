import time, datetime


class DataHelper:

    def __init__(self):
        pass

    # map_1中的值和map2中的diff，并且忽略ignore里的存在的key，返回map1中diff的kv
    @staticmethod
    def map_diff(map_1, map_2, ignore_map):
        diff_map = {}

        for k, v in map_1.items():
            if ignore_map.get(k) is not None:
                continue
            if map_2.get(k) != v:
                diff_map[k] = v
        return diff_map

    # map_1中的值和map2中的diff，并且忽略ignore里的存在的key，返回map1中diff的kv
    # sa需要特殊处理，如果没有替换的key，则不会进行传入kafka该字段
    @staticmethod
    def map_obj_diff(map_attr, obj, need_columns, unique_attr, replace_map={}, extar_list=[], source=""):
        map_1 = map_attr.copy()
        if need_columns is None:
            return {
                'diff': {},
                'data': {},
                'change': {},
            }
        diff_map = {}
        change_map = {}
        # 处理新增逻辑
        if obj is None:
            for k, v in need_columns.items():

                if map_1.get(k, None) is None:
                    map_1[k] = None

                is_continue = False
                if k in unique_attr.keys():
                    change_map[v] = map_1.get(k)
                    is_continue = True

                if replace_map.get(k) is not None and replace_map.get(k) in map_1.keys():
                    map_1[k] = map_1.get(replace_map.get(k))

                if is_continue:
                    continue

                change_map[v] = map_1.get(k)
                change_map[v + '_old'] = None

            # for k,v in extr_map.items():
            #     if k in map_1.keys() and v in map_1.keys():
            #         map_1[v]=map_1[k]

            return {
                "diff": map_1,
                "data": map_1,
                'change': change_map,
            }

        for k, v in map_1.items():
            if hasattr(obj, k) is False:
                continue
            ov = getattr(obj, k)
            if isinstance(ov, datetime.datetime) or isinstance(ov, datetime.date) or isinstance(ov, datetime.time):
                ov = str(ov)

            if ov != v:
                diff_map[k] = v

            sync_key = need_columns.get(k)
            if sync_key is not None:
                if k in unique_attr.keys():
                    change_map[sync_key] = v
                    continue

                change_map[sync_key] = v
                change_map[sync_key + '_old'] = ov

        # 因为添加强制同步功能，特注释掉此处
        # if len(diff_map) == 0:
            # return {
            #     'diff': {},
            #     'data': {},
            #     'change': {},
            # }

        item = {}
        for k, sync_k in need_columns.items():

            # 处理记录change_record数据
            if k in unique_attr.keys():
                change_map[sync_k] = getattr(obj, k)
            else:
                if k in map_1.keys() and hasattr(obj, k):
                    change_map[sync_k] = map_1.get(k)

                    # 日期格式转为字符串
                    ov = getattr(obj, k)
                    if isinstance(ov, datetime.datetime) or isinstance(ov, datetime.date) or isinstance(ov,
                                                                                                        datetime.time):
                        ov = str(ov)
                    change_map[sync_k + '_old'] = ov
                elif k not in map_1.keys() and hasattr(obj, k):
                    ov = getattr(obj, k)
                    # 日期格式转为字符串
                    if isinstance(ov, datetime.datetime) or isinstance(ov, datetime.date) or isinstance(ov,
                                                                                                        datetime.time):
                        ov = str(ov)
                    change_map[sync_k] = ov
                    change_map[sync_k + '_old'] = ov

            if k in map_1.keys():
                item[k] = map_1.get(k, None)
            else:
                if hasattr(obj, k):
                    ov = getattr(obj, k, None)
                    # 日期格式转为字符串
                    if isinstance(ov, datetime.datetime) or isinstance(ov, datetime.date) or isinstance(ov,
                                                                                                        datetime.time):
                        ov = str(ov)
                    item[k] = ov
                else:
                    item[k] = map_1.get(k, None)

            if replace_map.get(k) is not None:
                if replace_map[k] in map_1.keys():
                    item[k] = map_1.get(replace_map.get(k))
                elif source != 'sa' and hasattr(obj, replace_map.get(k)):
                    item[k] = getattr(obj, replace_map.get(k))


            # if extr_map.get(k) is not None and extr_map.get(k) in map_1.keys():
            #     item[k] = map_1.get(extr_map.get(k))

        for k in extar_list:
            if k in map_1.keys():
                item[k] = map_1[k]

        return {
            "diff": diff_map,
            "data": item,
            'change': change_map,
        }

    @staticmethod
    def map_diff_data(map_1, map_2, need_column):
        diff_map = {}

        for k in need_column:
            if map_1.get(k) == map_2.get(k):
                continue
            diff_map[k] = map_1.get(k)
        return diff_map

    @staticmethod
    def map_need_data(map_1, map_2, need_column):
        diff_map = {}

        for k in need_column:
            if map_1.get(k) == map_2.get(k):
                continue
            diff_map[k] = map_1.get(k)
        return diff_map

    @staticmethod
    def map_obj_diff_data(map_1, obj, check_column):
        diff_map = {}

        for k in check_column:
            if map_1.get(k) == obj.getattr(k):
                continue
            diff_map[k] = map_1.get(k)
        return diff_map


data_helper = DataHelper()
