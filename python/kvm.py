#-*- coding:utf-8 -*-
import os
def login():
	a = """
----------------------
\033[1;32;40m\t1.创建虚拟机
\t2.启动虚拟机
\t3.删除单个虚拟机
\t4.添加硬盘
\t4-1.移除硬盘
\t5.添加网卡
\t5.1动态添加cpu
\t5.2动态添加内存
\t6.查询当前虚拟机状态
\t7.关闭虚拟机
\t8.退出
----------------------
"""
	print a.center(5000)
	test()
def test():
	chaxun = os.popen("virsh list --all").read()
	in_put = raw_input("> ")
	if in_put == '6':
		print chaxun
		login()
	elif in_put == '1':
		print "创建虚拟机个数是:"
		in_put_1 = raw_input("> ")
		n = 1
		print "名称"
		in_put_2 = raw_input("> ")
		while int(in_put_1) >= n:
			in_put_3 = in_put_2 + '-' + str(n)
			os.popen("virt-clone -o test -n "+in_put_3+" -f /home/work/kvm/"+in_put_3+".img").read()
			n = n + 1
		login()
	elif in_put == '2':
		print "启动虚拟机的名称:"
		in_put_1 = raw_input("> ")
		os.popen("virsh start "+in_put_1+"").read()
		print "启动成功"
		login()
	elif in_put == '3':
		print "输入要删除虚拟机的名称:"
		in_put_1 = raw_input("> ")
		os.popen("virsh destroy "+in_put_1+"").read()
		os.popen("virsh undefine "+in_put_1+"").read()
		os.popen("rm -f /home/work/kvm/"+in_put_1+".img")
		print "删除成功并清空了目录img文件"
		login()
	elif in_put == '4':
		print "请输入要添加的硬盘大小(单位GB如1G，100G，1000G):"
		in_put_1 = raw_input("> ")
		print "再输入要给硬盘命名的名称:"
		in_put_2 = raw_input("> ")
		kvm_disk =os.popen("ls /home/work/kvm_disk > /home/work/1.txt").read()
		kvm_disk_txt = os.popen("cat /home/work/1.txt").read()
		if in_put_2 in kvm_disk_txt:
			print "已有此块硬盘，退出"
			login()
		else:
			pass		
		os.popen("qemu-img create -f qcow2 /home/work/kvm_disk/"+in_put_2+".img "+in_put_1+"").read()
		print "请输入要挂载的虚拟机名称:"
		in_put_3 = raw_input("> ")
		os.popen("virsh attach-disk "+in_put_3+" --source /home/work/kvm_disk/"+in_put_2+".img --target vdb --cache writeback --subdriver qcow2 --persistent").read()
		print "---------------------"
		os.popen("virsh domblklist "+in_put_3+"").read()
		login()
	elif in_put == '4-1':
		print "输入要移除硬盘虚拟机的名称:"
		in_put_1 = raw_input("> ")
		os.popen("virsh detach-disk "+in_put_1+" vdb --persistent").read()
#		os.popen("rm -f /home/work/kvm_disk/"++"")
		print "成功"
		login()
	elif in_put == '5':
		print "未完成"
		pass
	elif in_put == '5.1':
		print chaxun
		print "输入为哪台虚拟机增加cpu"
		in_put_1 = raw_input("> ")
		print "此台虚拟机CPU情况如下"
		cpuinfo= os.popen("virsh dominfo "+in_put_1+"").read()
		print cpuinfo
		print "为此台虚拟机添加几块cpu，注意动态添加只可增不可减"
		in_put_2 = raw_input("> ")
		os.popen("virsh setvcpus "+in_put_1+" "+in_put_2+"").read()
		cpuinfo_1 = os.popen("virsh dominfo "+in_put_1+"").read()
		print cpuinfo_1
		print "完毕"
		login()
	elif in_put == '5.2':
		print chaxun
		print "请输入为哪台虚拟机增加内存"
		in_put_1 = raw_input("> ")
		print "此台虚拟机内存情况如下"
		meminfo = os.popen("virsh dominfo "+in_put_1+"").read()
		print meminfo
		print "为此台虚拟机添加几G内存，注意单位为G，例：输入1G"
		in_put_2 = raw_input("> ")
		os.popen("virsh setmem "+in_put_1+" "+in_put_2+"").read()
		meminfo_1 = os.popen("virsh dominfo "+in_put_1+"").read()
		print meminfo_1
		print "完毕"
		login()
	elif in_put == '7':
		print "输入要关闭的虚拟机名称:"
		in_put_1 = raw_input("> ")
		os.popen("virsh destroy "+in_put_1+"").read()
		print "关闭完毕"
		login()
	elif in_put == '8':
		exit(0)
	else:
		print "不知你在说啥"
		login()
login()
