from random import randint, choice
from PIL import Image, ImageDraw, ImageFont

# 生成随机点坐标
def randomPoint(img):
    # 需要注意他们的取值范围
    return randint(0, img.width), randint(0, img.height)


# 生成随机颜色
def randomColor(start=0, end=255):
    return randint(start, end), randint(start, end), randint(start, end)


# 生成两个随机点坐标
def randomPoints(img):
    x0, y0 = randomPoint(img)
    x1, y1 = randomPoint(img)
    # 确保 x1 >= x0 和 y1 >= y0
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    return (x0, y0), (x1, y1)


# if __name__ == '__main__':
def create_code():
    # 首先创建一个画布，选择RGB模式，图片尺寸我这里设置为长400，高200，颜色为白色,等价于(255, 255, 255)
    img = Image.new(mode="RGB", size=(400, 220), color="white")

    # 创建画笔,在图片上绘制图形
    pen = ImageDraw.Draw(img, mode="RGB")
    pen.point((200, 100), fill="black")

    for i in range(img.width * img.height // 8):
        pen.point(randomPoint(img), randomColor(150))

    for i in range(randint(10, 16)):
        # 直线第一个参数是起始坐标与终点坐标(元组形式)
        # 第二个参数指定颜色,第三个参数指定直线的粗细
        pen.line(randomPoints(img), fill=randomColor(), width=randint(1, 3))
        pen.arc(randomPoints(img), 0, randint(0, 180), fill=randomColor())
    myfont = ImageFont.truetype("D:\APP\VS CODE\web\department\hanshand.ttf", size=90)
    total = 5  # 定义验证码长度
    part = img.width // (total + 2)  # 将图片等分为n+2分
    pos = 0  # 相当于指针，指在哪个地方哪个地方就填入对应字符
    res = []
    for i in range(total):
        pos += part  # 每次循环移动一次指针方便字符写入
        # 先随机生成一个65~90的数字使用chr将其转换成A~Z的字符，再随机生成一个0~9数字，最后再在二者选其一。
        r = choice((chr(randint(65, 90)), str(randint(0, 9))))
        res.append(r)
        # 对于我这个字体样式而言，高度在八分之三的位置比较合适，高度可以根据自己的字体样式自行调整
        pen.text((pos, 3 * img.height // 8), text=r, fill=randomColor(30, 200), font=myfont)
    res = ''.join(res)
    # img.show()
    # print(res)
    # 路径换成自己想保存的位置
    # with open(r"yzm.png", "wb") as fp:
    #     img.save(fp, format="png")
    return img,res
