#!/usr/bin/python
#-*- coding:utf-8 -*-
from sys import argv

def tools():
	print "你好，旅行者，欢迎来到道具屋！arms or weapon."
	
	cold_steel = ["倚天屠龙刀", "小刀", "大刀", "双立人菜刀"]
	guns = ["AK47", "沙漠之鹰", "M4A1"]
		
	next = raw_input("> ")
	if "arms" in next:
		for cold_steel_1 in cold_steel:
			print "武器: %s" % cold_steel_1
		next_1 = raw_input("> ")
#		for cold_steel_1 in cold_steel:
		if "小刀" in next_1 or "倚天屠龙刀" in next_1 or "大刀" in next_1 or "双立人菜刀" in next_1:
#		if cold_steel_1 == next_1:
			print "出发吧，前往初级试炼!"
			evil()
		else:
#			dead("请选择列出的武器，并重新运行程序，谢谢.")
			print "请选择列出的武器，并重新进入房间，谢谢."
			start()	
	elif "weapon" in next:
		for gun in guns:
			print "武器: %s" % gun
		next_1 = raw_input("< ")
		for gun in guns:
#			next_1 = raw_input("< ")
			if next_1 == gun:
				print "出发吧，前往中级试炼!"				
				ags()
			else:
				pass
		dead("请先练习识字并重新运行程序！")	
#			print "请选择列出的武器，并重新运行程序，谢谢."
#			start()
	
	else:
		print "请选择arms或者weapon！"
		tools()

def replenishment():
	print "你好，旅行者，有什么可以帮助你的?"
	print "我们这出售各类血瓶."
	print "------------"
	print """
小红
金创药
云南白药
"""
	print "------------"
	next = raw_input("< ")
	if next == "小红" or next == "金创药" or next == "云南白药":
		print "去吧前往大厅准备迎接试炼！"
		start()
	else:
		print "请选择列表中的物品."
		replenishment()

def evil():
	print "温磬提示，次房间涉及输出有，攻击，防御，逃跑."
	print "哈哈，看看是谁来了，又一个可怜虫."
	print "代表黑暗消灭你!"
	evil_moved = False
	while True:
		next = raw_input("< ")
		if next == "逃跑":
			dead("你被邪恶的小怪击杀")
		elif next =="攻击" and not evil_moved:
			print "对小怪造成了100点伤害，小怪对你造成50点伤害，你的HP剩余150."
			evil_moved = True
#			print not evil_moved
		elif next == "攻击" and evil_moved:
			dead("小怪进行防御触发反击，对你造成150点暴击伤害，你死了.")
		elif next == "防御" and evil_moved:
			print "小怪对你进行攻击，你完美防御，并触发反击对小怪造成100000点暴击伤害."
			ags()
		else:
			print "我无法识别你输入的字符，请参照温馨提示进行输入！"

def ags():
	print "温馨提示，次房间的输出命令与上一关一致."
	print "我是魔王阿古斯，臭虫."
	print "来吧，让我送你去地狱."
	skill = ["攻击", "防御", "逃跑", "斩杀"]
	abc = True
	for skill_1 in skill:
		print "技能表: %s" % skill_1
	for skill_1 in skill:
		next_1 = raw_input("< ")
		if next_1 == "攻击" and abc:
			print "你对阿古斯造成100点伤害对方进行反击，你的HP剩余100."
			abc = False
		elif next_1 == "攻击" and not abc:
			print "你对阿古斯造成暴击，阿古斯晕眩!"
			abc = True
		elif next_1 == "斩杀" and abc:
			print "你拯救了世界去拿你的奖励吧！"
			gold_room()
		elif next_1 == "防御":
			dead("你死了，阿古斯对你造成暴击伤害100000000000!")
		elif next_1 == "逃跑":
			dead("在你逃跑的路上阿古斯对你释放死亡缠绕!")
		else :
			pass
			dead("我无法识别你输入的字符，请参照温馨提示进行输入!")

def gold_room():
	dead("获取黄金若干美女若干.")

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	script, filename = argv
	txt = open(filename)
	print "这是我新建的小游戏: %s" % filename
	print txt.read()
	
	next = raw_input("< ")
	
	if next == "tools":
		tools()
	elif next == "replenishment":
		replenishment()
	elif next == "evil":
		evil()
	elif next == "ags":
		ags()
	else:
		dead("你还没有准备好吗，旅行者，请重新运行程序!")

start()
