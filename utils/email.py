import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

"""
RPC工具
"""


class Email:
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_port = "25"  # 设置服务器
    mail_user = "xxx"
    mail_pass = "xxx"
    sender = 'xxx'

    # 发送请求
    def sed_email(self, subject, title, content, receivers, subtype='plain'):
        message = MIMEText(content, subtype, 'utf-8')
        message['From'] = Header(title, 'utf-8')  # 发送者
        message['To'] = Header("", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, self.mail_port)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error:无法发送邮件")

    # 发送请求
    def sed_email_attach(self, subject, title, content, receivers, subtype='plain', path='',fname=''):
        msg = MIMEText(content, subtype, 'utf-8')
        message = MIMEMultipart()
        message["Subject"] = Header(subject, 'utf-8')
        message["From"] = Header(title, 'utf-8')  # 发送者
        message["To"] = Header("", 'utf-8')

        message.attach(msg)

        if fname != '':
            xlsxpart = MIMEApplication(open(path+fname, 'rb').read())
            basename = fname
            xlsxpart.add_header('Content-Disposition', 'attachment',
                                filename=('gbk', '', basename))  # 注意：此处basename要转换为gbk编码，否则中文会有乱码。
            message.attach(xlsxpart)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, self.mail_port)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error:无法发送邮件")


util_email = Email()
