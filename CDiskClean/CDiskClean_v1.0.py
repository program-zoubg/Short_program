import os, sys

try:
    file_r = open("C:/ProgramData/CDiskClean/User.dll", "r")
except:
    os.mkdir("C:/ProgramData/CDiskClean/")
    file = open("C:/ProgramData/CDiskClean/User.dll", "w")
    file.close()
    file = open("C:/ProgramData/CDiskClean/VIP.dll", "w")
    file.write("0")
    file.close()
    file_r = open("C:/ProgramData/CDiskClean/User.dll", "r")
file_r.close()
v = open("C:/ProgramData/CDiskClean/VIP.dll", "r")
vip = v.read()
if vip == "3":
    vip_n = "CDC_金榜VIP"
elif vip == "2":
    vip_n = "CDC_超级VIP"
elif vip == "1":
    vip_n = "CDC_银榜VIP"
else:
    vip_n = "普通用户"
v.close()

print("========================-The CDiskClean open-========================")
print("版本：v1.0")
print(f"我的会员状态：{vip_n}")
print()
print("1. C盘标准清理")
print("2. C盘缓存嗅探清理")
print("3. C盘深度清理")
print("0. Exit(退出)")
while True:
    num = input("请输入操作选项：")
    if num == "0":
        sys.exit(0)
    elif num == "1":
        print("正在运行标准清理...")
        for f in os.listdir("C:/Windows/Temp/"):
            f = "C:/Windows/Temp/" + f
            try:
                os.remove(f)
            except:
                continue
        print("清理完成...")
    elif num == "2":
        print("正在运行缓存嗅探清理...")
        for f in os.listdir("C:/Windows/Temp/"):
            f = "C:/Windows/Temp/" + f
            try:
                os.remove(f)
            except:
                continue
        for f in os.listdir("C:/Users/ADMINI~1/AppData/Local/Temp/"):
            f = "C:/Users/ADMINI~1/AppData/Local/Temp/" + f
            try:
                os.remove(f)
            except:
                continue
        print("清理完成...")
    elif num == "3":
        if int(vip) >= 1:
            print("正在开始...")
            file_l = os.listdir("C:/Windows/debug/")
            for l in file_l:
                try:
                    os.remove("C:/Windows/debug/" + l)
                except:
                    continue
            file_l = os.listdir("C:/Windows/SystemTemp/")
            for l in file_l:
                try:
                    os.remove("C:/Windows/debug/SystemTemp/" + l)
                except:
                    continue
            for f in os.listdir("C:/Windows/Temp/"):
                f = "C:/Windows/Temp/" + f
                try:
                    os.remove(f)
                except:
                    continue
            for f in os.listdir("C:/Users/ADMINI~1/AppData/Local/Temp/"):
                f = "C:/Users/ADMINI~1/AppData/Local/Temp/" + f
                try:
                    os.remove(f)
                except:
                    continue
            print("完成！")
        else:
            print("本操作需要银榜VIP以上才有资格体验...")
