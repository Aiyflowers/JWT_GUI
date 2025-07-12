#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/8 23:05
# @Author : Aiyflowers


import base64


# 初始化base64——padding代码，防止base64报错
def init_padding(jwt):
    my_jwt = jwt.split('.')
    print(my_jwt)
    for i in range(len(my_jwt)):
        # 这里是为了避免base64解码时候padding报错，需要补= 使用url_safe_b64decode就可以了
        temp_yushu = len(my_jwt[i]) % 4
        if temp_yushu != 0:
            # print("补充=号前：", my_jwt[i])
            my_jwt[i] += '=' * (4 - temp_yushu)
            # print("补充=号后：", my_jwt[i])
        if i == 2 :
            print("修正base64——padding完成!")
            return my_jwt


# 提取headers
def get_headers(jwt):
    my_jwt = init_padding(jwt)
    headers = base64.urlsafe_b64decode(my_jwt[0]).decode('utf8')
    print("headers:", headers)
    return headers


# 提取payload
def get_payload(jwt):
    my_jwt = init_padding(jwt)
    print("这个长度为：",len(my_jwt[1]))
    payload = base64.urlsafe_b64decode(my_jwt[1]).decode('utf8')
    print("payload:", payload)

    return payload


# 提取signature jwt第三部分
def get_signature(jwt):
    my_jwt = init_padding(jwt)
    print("signature:", my_jwt[2])
    return my_jwt[2]


# 将修改后的jwt重新加密，之所以这么写是为了后期和pyqtUI联动
def r_encode(jwt):
    print("--------------->提示：正在为你进行加密jwt<----------------\n")
    headers = get_headers(jwt)
    headers = base64.urlsafe_b64encode(headers).decode('utf8')
    payload = get_payload(jwt)
    payload = base64.urlsafe_b64encode(payload).decode('utf8')
    signature = get_signature(jwt)
    new_jwt = f'{headers}.{payload}.{signature}'
    print(new_jwt)
    print("--------------->提示：加密jwt完成<----------------\n")
    return new_jwt


