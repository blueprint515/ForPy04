# -*- coding: utf-8 -*-

import random
num = random.randint(0,20)

print ("开始猜数字")

for i in range(1,11):
    guess_num = int(input("请输入20以内的数字： "))
    n = 10 - i
    if guess_num > num:
       print ("您猜的数字大了！请重新输入20以内数字：\n您还剩{0}次机会".format(n))
    elif guess_num < num:
       print ("您猜的数字小了！请重新输入20以内数字：\n您还剩{0}次机会".format(n))
    else:
         print ("恭喜您猜对了！") 