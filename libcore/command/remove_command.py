#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class RemoveCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        return None


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
