#1gui(图形用户界面)
'''
import easygui#gui头文件
flavor=easygui.enterbox('你喜欢吃的？',default='西瓜')#询问弹窗，默认值西瓜
easygui.msgbox('你喜欢的是',flavor)
'''
#2猜数
'''
import easygui#gui头文件
az=easygui.integerbox ('请输入你猜的数')#1只能1~99
'''
#3询问年龄
'''
if=检测
elif=再次检测
elsc=都不等于
'''
'''
import easygui#gui头文件
age1=easygui.enterbox('你的年龄是？')#询问
age2=float(age1)
if age2>=18:#年龄判断,大于18
    print('你的年龄大于18')
elif 14<age2<18:#年龄判断，小于18，大于14
    print ('你的年龄小于18，大于14')
elif age2<=14:#年龄判断，小于14
    print ('你的年龄小于14')
'''
#4双重判断
import easygui#gui头文件
age1=easygui.enterbox('你的年龄是？')#询问年龄
age2=float(age1)#转化数据为整形
if age2>=18:#年龄判断,大于18
    shen_gao1=easygui.enterbox('你的身高是多少？')#询问身高
    shen_gao2=float(shen_gao1)#转化数据为整形
    if shen_gao2>=175:#判断身高
        print ('筛选通过！')
    else:
        print ('你的身高小于175，筛选不通过！')
else:#年龄判断，小于18
    print ('你的年龄小于18，筛选不通过！')
