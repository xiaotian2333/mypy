import easygui#gui头文件

#1无聊的东西
'''
da_an=12
da_an1=easygui.enterbox('答案是什么')
da_an2=float(da_an1)#转化数据为整形

if da_an2==da_an:#答案判断，正确
    print ('答案正确')
    
else:#答案判断，错误
    print ('答案错误')
'''

#2降价促销
'''
一家商场在降价促销，如果购买金额小于或等于 10 元，
会给 20% 的折扣，如果购买金额大于 10 元，会给 10% 的折扣。
编写一个程序，询问购买价格，再显示最终价格。
'''
'''
jia_ge1=easygui.enterbox('价格是多少')
jia_ge2=float (jia_ge1)#转化数据为整形

if jia_ge2<=10:
    print ('打折前价格：'+jia_ge1+'打折后价格：'+str(jia_ge2-(jia_ge2*0.2)))

else:
    print ('打折前价格：'+jia_ge1+'打折后价格：'+str(jia_ge2-(jia_ge2*0.1)))
'''
#3寻找年龄
'''
一个足球队在寻找年龄 10 岁到 20 岁之间的小女孩加入，
编写一个程序，询问用户的年龄和性别（m表示男性，f表示女性）。
显示一条消息指出这人是否可以加入球队。
'''
nian_ling1=easygui.enterbox('你的年龄是多少？')
nian_ling2=float(nian_ling1)#转化数据为整形
xing_bie=easygui.buttonbox('你的性别是？',choices=['男','女'])#选择弹窗，用户体验非常nice
if 9<nian_ling2<21 and xing_bie=='女':#蛋疼的判断
    print('可以加入')
else:
    print('不可以加入')
