for i in repr('10'):  #for循环，字符记得加隐，缩进冒号
    val = input('请输入带温度表述符号的温度值（例如：32C或95F）:\n')
    if val[-1] in ['C','c']:       #in 为二元关系操作，判断左侧内容是否在右侧集合中
        f = 1.8 * float (val [0:-1])+32    #float为浮点函数，将字符串变成一个小数
        print("转换后的温度为：%.2fF"%f)
    elif val [-1] in ['F','f']:
        c = (float (val [0:-1]) - 32) / 1.8
        print("转换后的温度为：%.2fC"%c)

    else:
        print("输入有误")