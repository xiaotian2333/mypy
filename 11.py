#1计算三角形的面积
'''
print('请输入三角形的高')#要求用户输入
gao=input()
print('请输入三角形的底边长')
bian=input()

print('面积=');print(gao*bian/2)#计算
'''

#2计算圆的面积
'''
print('请输入圆的半径')#要求用户输入
r=input()

print('面积=');print(3.14*r*r)#计算
'''

#3判断奇数偶数
'''
print('请输入要判断的数')#要求用户输入
shu=int(input())

if shu%2!=0:
    print('this j')#奇数
else:
    print('this o')#偶数
'''

#4判断闰年
'''
print('请输入要判断的年份')#要求用户输入
shu=int(input())

if shu%4!=0:
    print('this no')#不是闰年
else:
    print('this yes')#润年
'''

#5九九乘法表
'''
for i in range(1,10):#第一个数
    print('\n')
    for x in range(1,i+1):#第二个数
        print(str(i)+'x'+str(x)+'='+str(i*x))
'''

#6简单计算机

print('输入第一个数')
shu_1=input()
print('输入第二个数')
shu_2=input()
fs=input('选择计算方式(1=加,2=减,3=乘,4=除)')

#加
if fs==1:
    print(shu_1+shu_2)
elif fs==2:
    print(shu_1-shu_2)
elif fs==3:
    print(shu_1*shu_2)
elif fs==4:
    print(shu_1/shu_2)
