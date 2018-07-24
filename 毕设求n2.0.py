for i in repr('20'):
    N = input('请输入N的值：')
    DM = 0.417*float(N)/(1+(float(N)-1)*0.417)
    Dm = 0.167 * float(N) / (1 + (float(N) - 1) * 0.167)
    print("DM = %.3f\n"%DM )
    print("Dm = %.3f\n" % Dm )