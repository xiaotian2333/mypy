#1乘法表
'''
x=5
for i in range(1,11):
    print(i,'x',x,'=',i*x)
'''

#2用户自定义循环
'''
num=int(input('你想要多少个*'))
for i in range(1,num+1):
    print('*',end='')
'''

#3瞎鸡巴蛋疼的东西
'''
numlines=int(input('一共要多少行'))
numstars=int(input('每行多少星星'))
for line in range(0,numlines):
    print('\n')
    for star in range(0,numstars):
        print('*',end='')
'''

#4小心电脑！
'''
for u in range(0,21):
    for i in range(0,21):
        for o in range(0,21):
            print(u,i,o)
'''

#5课后练习
'''
for i in range(5):
    for j in range(3):
        print('*',end='')

numlines=int(input('要多少？'))
for i in range(0,numlines):
    for j in range(3):
        print('*',end='')
'''

#6可自定义的计数器

num=int(input('倒计时多少'))
import time
for i in range(num,0,-1):
	print(i)
	time.sleep(1);
print('计数完毕')
