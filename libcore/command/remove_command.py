#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class RemoveCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        # TODO 通过 ctx.params 获取 用户参数字典，再通过字典关键字获取对应值，判断后调用cache删除缓存/已安装
        a = ctx.params
        print(a)
        pass


class RemoveCommandCacheOption(click.Option):
    pass


class RemoveCommandallOption(click.Option):
    pass


class RemoveCommandInstallOption(click.Option):
    pass


class RemoveCommandPublisherArgument(click.Argument):
    pass


class RemoveCommandVersionArgument(click.Argument):
    pass


if __name__ == '__main__':
    pass
