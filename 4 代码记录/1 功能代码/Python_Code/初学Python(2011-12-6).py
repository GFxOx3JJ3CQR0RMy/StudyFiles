#!/usr/bin/python
# -*- coding: UTF8 -*-
#Filename: using_sys.py


#-------------- import 的使用
#=======================
#import sys
#print 'The command line arguments are:'
#for i in sys.argv:
#    print i
#
#print '\n\nThe PYTHONPATH is',sys.path ,'\n'
#=======================

'''#传说三个单引号可以当做多行注释 别蛋疼了 凑合着用吧
#-------------- list 的使用
#============================
#！/usr/bin/python
#Filename: using_list.py

#******list 的使用比较蛋疼  与元组 的不同之处在于 列表是 可变的 数据类型
#       表示方式上  list 用方括号   而元组用的是圆括号
shoplist = ['apple','mango','carrot','banana']
print 'I have ',len(shoplist),'items to purchase.'
for item in shoplist:
    print item,

#**添加个 rice
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist

#**排序  shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is',shoplist

#**删除 买完的 apple
print 'The first item I will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist
'''


'''############希望新的python版本能出现多行注释吧 这种三个单撇的注释方法我实在是看着不顺眼啊
#----------------元组的使用
#!/usr/bin/python
#Filename:using_tuple.py
#*****蛋疼的元组有很多需要注意的问题
#**1）首先说元组的定义 是用圆括号 表示的，当元组的元素只有一个的时候括号内应该以 ‘逗号’结尾
#             比如：  zoo =('monkey',)
zoo = ('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)
#**2) 元组可以包含元组，但是下面的例子中 zoo 和monkey 却有着同样的地位
#             这一点在 跟着的print结果可以看出  len(new_zoo) 的结果是3
new_zoo = ('monkey','dolphin',zoo)
print 'Number of animals in the new zoo is',len(new_zoo)

print 'All animals in new zoo are',new_zoo
#**3） 元组的访问可以通过下标来访问，下表从0开始计数 所以zoo 的访问下标为2
#             需要特别注意的是 new_zoo[2][2]的用法 它访问的是new_zoo中zoo的elephant元素
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoois',new_zoo[2][2]
'''
'''##############################
#------------元组的使用还没完  看我继续抄代码

#!/usr/bin/python
#Filename:print_tuple.py
age = 22
name = 'Swaroop'
#  1) 当输出有两个或两个以上变量的时候 要使用圆括号括起来 当只有一个变量的时候可以不用圆括号
print '%s is %d years old' % (name, age)
print 'Why is %s playing with that python?' % name
'''