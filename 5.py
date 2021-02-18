#1计算地毯价格
'''
print ('请输入长度')
a=int(input ())#长度
print ('请输入宽度')
s=int(input ())#宽度
print ('长度',end='');print (a)
print ('········')
print ('宽度',end='');print (s)
print ('········')
print ('地毯',end='');print (a*s)
print ('········')
print ('地毯的价格是多少？')
d=int (input ())#地毯的价钱
print ('地毯总共',end='');print (a*s*d,end='');print ('元')
'''

#2GUI（图形用户界面）
'''
import easygui#gui头文件
flavor=easygui.choicebox('请选择你喜欢吃的',choices=['老八','蔡旭坤','老师'])#文本选择
flavor=easygui.buttonbox('请选择你喜欢吃的',choices=['老八','蔡旭坤','老师'])#选择弹窗
easygui.msgbox('你喜欢的口味是:'+flavor)#信息弹窗
flavor=easygui.enterbox('gaoi')#询问弹窗
easygui.msgbox('你是'+flavor)
'''
