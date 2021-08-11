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


image = get_file_content('1.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "https//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """

client.basicGeneralUrl(url, options)
for item in result.items():
    with open('result.txt','a+',encoding="utf-8") as f:
        f.writelines(str(item)+'\r\n')
