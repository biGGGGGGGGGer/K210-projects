from Maix import MIC_ARRAY as mic
import lcd
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

lcd.init()
mic.init()

northeast = [1,2,3]             # 东北
northwest = [10,11,12]          # 西北
southeast = [4,5,6]             # 东南
southwest = [7,8,9]             # 西南

fm.register(8,fm.fpioa.GPIO0)
IO1=GPIO(GPIO.GPIO0,GPIO.OUT)

fm.register(30,fm.fpioa.GPIO1)
IO2=GPIO(GPIO.GPIO1,GPIO.OUT)

fm.register(31,fm.fpioa.GPIO2)
IO3=GPIO(GPIO.GPIO2,GPIO.OUT)

fm.register(32,fm.fpioa.GPIO3)
IO4=GPIO(GPIO.GPIO3,GPIO.OUT)

fm.register(33,fm.fpioa.GPIO4)
IO5=GPIO(GPIO.GPIO4,GPIO.OUT)

fm.register(34,fm.fpioa.GPIO5)
IO6=GPIO(GPIO.GPIO5,GPIO.OUT)

fm.register(35,fm.fpioa.GPIO6)
IO7=GPIO(GPIO.GPIO6,GPIO.OUT)


i = 0
e = 0
c = 0
max = 0
min = 0
d = 0
e = 0
Str = ""


while True:
    IO1.value(1)
    IO2.value(1)
    IO3.value(1)
    IO4.value(1)
    IO5.value(1)
    IO6.value(1)
    IO7.value(1)
    imga = mic.get_map()    # 获取声音源分布图像
    b = mic.get_dir(imga)   # 计算、获取声源方向
    print(b)
    a = mic.set_led(b,(0,0,255))  # 配置 RGB LED 颜色值
    imgb = imga.resize(198,198)   #重新调整图像大小
    imgc = imgb.to_rainbow(1)     # 将图像转换为彩虹图像
    lcd.display(imgc)
    a = len(b)
    # 提取出来元组元素中不为零的下标最大值
    for i in range(0,a):
        if b[i] != 0:
            c = i
    max = c + 1
    #提取出来元组为零的下标最小值
    for d in range(0,a):
        if b[d] != 0:
            e = d
            break
    min = e + 1
    print("min = ",min)
    print("max = ",max)
    if min in northeast and max in northeast:
        print("东北")
        IO2.value(0)
    if min in northwest and max in northwest:
        print("西北")
        IO1.value(0)
    if min in southeast and max in southeast:
        print("东南")
        IO4.value(0)
    if min in southwest and max in southwest:
        print("西南")
        IO3.value(0)
    if min == 1 and max == 12:
        print("正北")
        IO5.value(0)
    if min == 9 and max == 10:
        print("正西")
        IO7.value(0)
    if min == 6 and max == 7:
        print("正南")
        IO6.value(0)

mic.deinit()
