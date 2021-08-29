# encoding=utf-8
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '24684483'
API_KEY = '8mhMvUtgAvzCbfsy59RD7GPN'
SECRET_KEY = 'cUmfXwuraFT6bZhGfwuHs68WTA9AIFAF'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('1c.jpg')

""" 调用通用文字识别（含位置高精度版） """
result=client.accurate(image);

""" 如果有可选参数 """
options = {}
options["recognize_granularity"] = "big"
options["detect_direction"] = "true"
options["vertexes_location"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（含位置高精度版） """
result=client.accurate(image, options)
print(result)