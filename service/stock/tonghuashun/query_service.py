import datetime
from utils import logger
from flask import current_app as app

"""
  球探数据存储服务
"""


class TonghuashunQueryService:
    def get_match_infos(self, match_ids):
        orm = QtMatch()
        matches = orm.query.filter(QtMatch.id.in_(match_ids)).all()  # .filter(SrCompetition.id < 30000).all()
        return matches


ths_qr_srv = TonghuashunQueryService()
