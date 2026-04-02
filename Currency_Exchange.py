'''根据业务需求，现需要你开发一个货币兑换系统
1. 实现人民币兑换美元的功能
2. 实现美元兑换人民币的功能
3. 实现人民币兑换欧元的功能
4. 兑换后保留两位小数
选择服务后要有波浪线分格

循环输出该服务系统,0结束程序,字典定义service_menu四种服务,使用items()返回键值对,if-else,结果打印
'''

service_menu = {
    1: "人民币兑换美元",
    2: "美元兑换人民币",
    3: "人民币兑换欧元"
} # 这是一个字典，键为服务编号，值为服务名称

controller = 1
while controller: # 这是一个循环，当controller为1时，循环继续

    for key,value in service_menu.items():
        print(f"{key}: {value}")
    
    func = input(f"请输入你需要的服务: ")
    print("====================================================================")
    choice = int(func)
    # 这是一个判断语句，根据用户输入的服务编号，执行不同的操作
    if choice == 1:
        amount = float(input("请输入你想兑换的人民币数额: "))
        usd = amount / 6.9
        print(f"您成功兑换{usd:.2f}美元")
    elif choice == 2:
        amount = float(input("请输入你想兑换的美元数额: "))
        rmb = amount * 6.9
        print(f"您成功兑换{rmb:.2f}人民币")
    elif choice == 3:
        amount = float(input("请输入你想兑换的人民币数额: "))
        eur = amount / 7.5
        print(f"您成功兑换{eur:.2f}欧元")
    else:
        print("您输入的选择有误,请重新输入")
        
    ask = int(input("是否继续兑换,0退出,其他继续"))
    if ask == 0:
        controller = 0
    else:
        continue




