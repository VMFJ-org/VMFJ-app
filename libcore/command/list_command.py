#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing as t

import click
import requests
from click import Context
from libcore.repository.index import App


class ListCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        app = App()
        get_ctx = ctx.params.get("publisher")
        # 获取本地与远程仓库所有JDK
        # remote_url = 'http://192.168.3.21:9908/apps/oracle/versions/17.0.5.json'
        # req = requests.get(remote_url)
        # res_json = req.json()
        # print(*res_json)
        set_ctx = app.set_os(get_ctx)
        print(set_ctx)

class ListCommandPublisherArgument(click.Argument):
    pass


if __name__ == '__main__':
    pass
