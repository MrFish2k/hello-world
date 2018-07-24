for i in  repr('20'):
    N = 1
    D = input('输入占空比：\n')

    Uo = 24*float(D)/(1+float(N)*(1-float(D)))
    print('Uo= %.3f'%Uo)