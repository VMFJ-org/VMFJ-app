#!/usr/bin/env python
# -*- coding:utf-8 -*-
import http

import requests
from libcore.repository.index import App

# remote_url = 'http://192.168.3.21:9908/apps/oracle/versions/17.0.5.json'
# req = requests.get(remote_url)
# res_json = req.json()
# list_i = []
# for i in res_json:
#     list_i.append(i["os"].lower())
# tuple_i = tuple(list_i)
# print(tuple_i)
#
app = App()
# a = app.get_publisher()
# print(a)

b = app.set_os(os="aaa")
print(b)

if __name__ == '__main__':
    pass
