#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


class App:
    __publisher = None
    __version = None
    __os = None
    __arch = None
    __dist = None
    __checksum_algo = None
    __checksum_content = None
    __file = None
    __remote_url = 'http://192.168.3.21:9908/apps/oracle/versions/17.0.5.json'

    # TODO Getter/Setter

    def get_os(self):
        req = requests.get(self.__remote_url)
        res_json = req.json()
        list_i = []
        for i in res_json:
            list_i.append(i["os"].lower())
        __os = tuple(list_i)
        return __os

    def set_os(self, os: str) -> str:
        curr_os = self.get_os()
        if os in curr_os:
            return os
        else:
            raise Exception("无此系统")

    def get_file(self) -> str:
        return self.__file


if __name__ == '__main__':
    pass
