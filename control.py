#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
import pymysql
import time
import api
import send

db = api.DataWord('localhost','root','root','EnglishWord','WE','mail')
 
'''
	查询数据库中所有的用户，并准备向他们发邮件
'''
mail = db.SelectMail()
for u in mail:
	UserMail = u[0]
	UserStart = u[1]
	NumId = u[2] + 1
	UserLimit = u[3]

	date = int(time.strftime("%H", time.localtime()))
	if date < 12:
		hi = 'Good morning'
	elif date < 18:
		hi = 'Good afternoon'
	else:
		hi = 'Good evening'

	# print(UserMail,UserStart,NumId,UserLimit)

	
	'''
		删除用户
	'''
	# rm = db.DelMail('....@163.com')

	'''
		显示每个用户每日单词
	'''
	data = db.SelectWord(UserStart, UserLimit)
	content = '''
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8"> 
			<title>每日英语</title>
			<link rel="stylesheet" href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css">  
			<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
			<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>
		<div style="text-align:center;">
		<h3>{hi} this is your words today.</h3>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>英文</th>
					<th>音标</th>
					<th>中文</th>
				</tr>
			</thead>
			<tbody>
	'''.format(hi=hi)
	for e,s,c in data:
		content += '''
			<tr class="success">
				<td>{e}</td>
				<td>{s}</td>
				<td>{c}</td>
			</tr>
		'''.format(e=e,s=s,c=c.strip()).strip()

	if UserStart != 0:
		YesterdayStart = UserStart - UserLimit
		if YesterdayStart < 0:
			YesterdayStart = 0
		YesterdayData = db.SelectWord(YesterdayStart, UserLimit)
		content += '''
		</tbody>
		</table>
		</div>
		<div style="text-align:center;">
		<h3>And this is your yesterday words.</h3>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>英文</th>
					<th>音标</th>
					<th>中文</th>
				</tr>
			</thead>
			<tbody>
		'''
		for x,y,z in YesterdayData:
			content += '''
				<tr class="success">
					<td>{x}</td>
					<td>{y}</td>
					<td>{z}</td>
				</tr>
			'''.format(x=x,y=y,z=z.strip()).strip()
			

	content += '''
		</tbody>
		</table>
		</div>
		</body>
		</html>
	'''

	# print(content)
	# break

	'''
		为每个用户发送单词
	'''
	user = send.SendMail(UserMail, content)
	user.DoSend('html')

	'''
		更新每个用户的起始单词id
	'''
	if NumId >= 4:
		NumId = 0
		UpdateStart = UserStart + 10
		text = db.UpdatetMail(UpdateStart, NumId, UserMail)
	else:
		text = db.UpdatetMail(UserStart, NumId, UserMail)

'''
	添加邮箱
'''
# add = db.AddMail('....@qq.com')