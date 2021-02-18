#高级计算机
while True:
    
    #询问模块
    fs=int(input('选择计算方式(0=停止,1=加,2=减,3=乘,4=除,5=求余,6=小学题计算模式)'))
    if fs==0:#停止
        print('正在退出')
        print('\n')
        break
    elif fs==6:#小学题计算模式
        tsfs=int(input('请选择方式(1=计算面积,2=计算地毯等物品价格)'))
        if tsfs==1:#计算面积
            a=int(input ('请输入长度'))#长度
            s=int(input ('请输入宽度'))#宽度
            print('面积',end='')
            print(a*s)
            print('\n')
            continue
        
        elif tsfs==2:#计算地毯、地板、草皮等价格
            a=int(input('请输入长度'))#长度
            s=int(input('请输入宽度'))#宽度
            d=int(input('物品的价格是多少？'))#物品的价钱
            print('物品总共',end='');print(a*s*d,end='');print('元')
            print('\n')
            continue

    shu_1=int(input('请输入第一个数'))
    shu_2=int(input('请输入第二个数'))

    #常规计算模块
    if fs==1:#加
        print(shu_1+shu_2)
        print('\n')
    elif fs==2:#减
        print(shu_1-shu_2)
        print('\n')
    elif fs==3:#乘
        print(shu_1*shu_2)
        print('\n')
    elif fs==4:#除
        print(shu_1/shu_2)
        print('\n')
    elif fs==5:#求余
        print(shu_1/shu_2%2)
        print('\n')

    else:#报错
        print('计算方式错误')
        print('\n')
