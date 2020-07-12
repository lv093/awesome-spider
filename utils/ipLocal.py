import socket
import fcntl
import struct


class IpLocal():

    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except Exception as err:
            ip = ""
        finally:
            s.close()
        return ip


IpLocal = IpLocal()
