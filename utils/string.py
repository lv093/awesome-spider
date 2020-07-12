import unicodedata
import hashlib

"""
字符串工具
"""


class String:
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def md5(self, input):
        if not isinstance(input, str):
            return ""

        uuid = hashlib.md5()
        uuid.update(input.encode('utf-8'))
        return uuid.hexdigest()


util_string = String()
