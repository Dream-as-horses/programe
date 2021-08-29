# encoding:utf-8
import os
import requests
import base64
from PIL import Image
i = 1
'''
图像主体检测
'''
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
access_token = '24.1f8a92ce1ad3707d7657396abb7bff45.2592000.1631585948.282335-24697075'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
#修改路径实现批量识别：
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        if 'jpg' in name:
            path = r't\{}.jpg'.format(i)
            image_name = os.path.join(root, name)[2:]
            f = open(image_name, 'rb')#路径打开
            img = base64.b64encode(f.read())
            params = {"image": img, "with_face": 1}
            response = requests.post(request_url, data=params, headers=headers)
            if response:
                ans = response.json()
                ans = ans['result']
            img = Image.open(image_name)
            cropped = img.crop((ans['left'], ans['top'], ans['width'], ans['height']))  # (left, top, width, height)
            cropped.save(path)  # 存储为图像.jpg"
            basewidth = 1920
            img = Image.open(path)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(path)
            i+=1





