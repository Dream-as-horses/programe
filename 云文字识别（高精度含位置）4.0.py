# encoding=utf-8
from aip import AipOcr
import os
""" 你的 APPID AK SK """
APP_ID = '24684483'
API_KEY = '8mhMvUtgAvzCbfsy59RD7GPN'
SECRET_KEY = 'cUmfXwuraFT6bZhGfwuHs68WTA9AIFAF'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        if 'jpg' in name:
            filePath = os.path.join(root, name)[2:]

            options = {
                'recognize_granularity': 'big',
                'detect_direction': 'true',
                'vertexes_location':'true',
                'probability':'true',
            }
            result = client.accurate(get_file_content(filePath), options);

            try:
                # for i in result['words_result']:
                #     print(i['words'])
                with open('result.txt', 'a+', encoding="utf-8") as f:
                    f.writelines(str(result) + '\r\n')
            except KeyError:
                print('识别错误')

