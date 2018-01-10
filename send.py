#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

class SendMail(object):
	"""
		此类是基于廖雪峰老师网上的教程做成的
		FormatAddr 是用于显示发件人和收件人信息的函数
		Dosend 是用于发送邮件的主函数
	"""
	def __init__(self, mail, conter, name='Memo'):
		self.mail = mail
		self.conter = conter
		self.name = name

	'''
		msg 为传入的发件人名字及邮箱或者收件人名字及邮箱
	'''		
	def FormatAddr(self, msg):
	    name, addr = parseaddr(msg)
	    return formataddr((Header(name, 'utf-8').encode(), addr))

	'''
		SendType 是指发送文本的格式
	'''
	def DoSend(self, SendType='plain'):
		from_addr = '....@163.com'
		password = '你的邮箱授权码'
		smtp_server = 'smtp.163.com'
		to_addr = self.mail
		befrom = '每日英语 <%s>' % from_addr
		to = '{name} <{mail}>'.format(name=self.name,mail=to_addr)

		msg = MIMEText(self.conter, SendType, 'utf-8')
		msg['From'] = self.FormatAddr(befrom)
		msg['To'] = self.FormatAddr(to)
		msg['Subject'] = Header('Your English words...', 'utf-8').encode()

		server = smtplib.SMTP(smtp_server, 25)
		server.set_debuglevel(1)
		server.login(from_addr, password)
		server.sendmail(from_addr, [to_addr], msg.as_string())
		server.quit()

if __name__ == '__main__':
	pass