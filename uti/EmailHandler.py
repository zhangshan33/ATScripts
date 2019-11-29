# -*- coding: utf-8 -*-
# __author__ = "maple"


'''
发邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from settings import conf

from uti.LoggerHandler import logger


class EmailHandler(object):

    def read_report(self):
        f = open(conf.TEST_CASE_REPORT_PATH, 'rb')
        return f.read()

    def send_email(self):
        """ 发送邮件 """

        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "1641839697@qq.com"  # 用户名
        mail_pass = "ygarpyvxlllgcbcc"  # 口令

        # 设置收件人和发件人
        sender = '1641839697@qq.com'
        receivers = ['1641839697@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例对象
        message = MIMEMultipart()

        # 邮件主题、收件人、发件人
        subject = '请查阅--测试报告'  # 邮件主题
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header("{}".format(sender), 'utf-8')  # 发件人
        message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # 收件人

        # 邮件正文内容 html 形式邮件
        send_content = self.read_report()  # 获取测试报告
        html = MIMEText(_text=send_content, _subtype='html', _charset='utf-8')  # 第一个参数为邮件内容

        # 构造附件
        att = MIMEText(_text=send_content, _subtype='base64', _charset='utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = 'report.html'
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
        message.attach(html)
        message.attach(att)

        try:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtp_obj.login(mail_user, mail_pass)
            smtp_obj.sendmail(sender, receivers, message.as_string())
            smtp_obj.quit()
            logger().info("邮件发送成功")

        except smtplib.SMTPException:
            logger().error("Error: 无法发送邮件")
