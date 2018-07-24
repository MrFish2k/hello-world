for i in repr('9'):
    week = "星期一星期二星期三星期四星期五星期六星期天"
    n = input("请输入天数(1-7):\n")
    N = (int(n)-1)*3
    we = week[N:N+3]
    print("此日日期为"+we+".")