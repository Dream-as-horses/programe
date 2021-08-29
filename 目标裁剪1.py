# encoding:utf-8

import requests
import base64

'''
图像主体检测
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
# 二进制方式打开图片文件
f = open('2c.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"with_face":1}
access_token = '24.1f8a92ce1ad3707d7657396abb7bff45.2592000.1631585948.282335-24697075'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

