#!usr/bin/python3

import json
import pymysql

'''
	关于单词和邮箱的处理
'''
class DataWord(object):
	"""
		docstring for DataWord
		获取每日单词，输出成字典格式
		获取每个mail用户的起始单词id
		更新每个mail用户的起始单词id，原起始id+10
	"""
	def __init__(self, host, user, passwd, db, wordtable='word', mailtable='mail', charset='utf8'):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.db = db
		self.wordtable = wordtable
		self.mailtable = mailtable
		self.charset = charset
		self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset )
		self.cursor = self.db.cursor()

	'''
		查询每日单词
		table : 单词表
		start : 起始单词id
		limit : 每日单词数
		返回元组
	'''
	def SelectWord(self, start, limit=10):
		sql = '''
			SELECT English,Chinese FROM {table} WHERE id > {start} LIMIT {limit}
		'''.format(table=self.wordtable,start=start,limit=limit).strip()
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
		except:
   			return "Error: unable to fetch data"

		return results

	'''
		查询每个mail用户的起始单词id
	'''
	def SelectMail(self):
		sql = '''
			SELECT mail,startid,LimitWord FROM {table}
		'''.format(table=self.mailtable).strip()
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
		except:
			return "Error: unable to fetch data"

		return results

	'''
		更新每个mail用户的起始id(id+10)
		默认起始单词id为0
	'''
	def UpdatetMail(self, start, mail):
		sql = '''
			UPDATE {table} SET `startid`='{start}' WHERE `mail` = '{mail}'
		'''.format(table=self.mailtable,start=start,mail=mail).strip()
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			return "Error: unable to update data"

		return 'successful'

	'''
		添加mail用户
	'''
	def AddMail(self, mail, limit=10):
		sql = '''
			INSERT INTO {table} (`mail`, `startid`, `LimitWord`) VALUES ('{mail}', '0', '{limit}')
		'''.format(table=self.mailtable,mail=mail,limit=limit).strip()
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			return "Error: unable to add mail"

		return 'successful'

	def DelMail(self, mail):
		sql = '''
			DELETE FROM {table} WHERE `mail`='{mail}'
		'''.format(table=self.mailtable,mail=mail).strip()
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			return "Error: unable to del mail"

		return 'successful'

	def __del__(self):
		self.cursor.close()
		self.db.close()


if __name__ == '__main__':

	db = DataWord('localhost','root','root','EnglishWord','word','mail')

	print('word'.center(50,'-'))
	data = db.SelectWord(0)
	for value in data:
		for x in value:
			print(x, end='\t')
		print()

	print('mail'.center(50,'-'))

	# add = db.AddMail('.....@163.com')
	# text = db.UpdatetMail('0','.....@163.com')
	# rm = db.DelMail('.....@163.com')
	mail = db.SelectMail()
	for value in mail:
		for x in value:
			print(x, end='\t')
		print()