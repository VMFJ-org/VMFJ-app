#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class InstallCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        print(ctx.params.get("publisher"))


class InstallCommandDownloadOnlyOption(click.Option):
    pass


class InstallCommandPublisherArgument(click.Argument):
    pass


class InstallCommandVersionArgument(click.Argument):
    pass


if __name__ == '__main__':
    pass
