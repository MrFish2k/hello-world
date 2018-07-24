for i in  repr('20'):
    N = input('输入N的值：\n')

    DM = (0.833+0.833*float(N))/(1+0.833*float(N))
    Dm =(0.083+0.083*float(N))/(1+0.083*float(N))
    print('最大占空比为:%.3f\n'%DM)
    print('最小占空比为：%.3f'%Dm)