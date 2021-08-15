from PIL import Image
koala = Image.open('1.jpg')
# 2,剪裁图像
# 设置左上，右下点的坐标4
rect =50, 1000, 960,1070
img=koala.crop(rect).    show()
img.save("res1.jpg")

