#!/usr/bin/env python
# -*- coding:utf-8 -*-
import click

from libcore.command.remove_command import *
from libcore.command.doctor_command import *
from libcore.command.use_command import *
from libcore.command.list_command import *
from libcore.command.install_command import *


class VMFJ:
    """
    命令行定义类
    """

    @staticmethod
    @click.group
    def vmfj():
        """
        定义函数为静态函数
        创建命令行组
        """
        pass

    @staticmethod
    def run():
        """
        定义函数为静态函数
        实现命令行参数、选项、帮助信息
        :return:无
        """
        # 通过命令行组的add_command方法创建remove子命令

        VMFJ.vmfj.add_command(cmd=RemoveCommand(
            name="remove",
            help="""
\n1. Delete the installed Java (delete the files and environment variables in the installation directory), but do not delete the cache. (--install | -i)
\n2. Delete the installed Java (delete the files and environment variables in the installation directory), but delete the cache. (--cache --install | -c -i)
\n3. Do not delete the installed Java, but delete the cache of the specified Java. (--cache | -c)
\n4. Do not delete the installed Java, but delete all caches.(--cache --all | -c -a)
\n5. --install | -i is default.
\n
\n For example:
\n  jjvmm remove Oracle
\n  jjvmm remove oracle
\n  jjvmm remove Oracle 19.0.1
\n  jjvmm remove --install Oracle
\n  jjvmm remove --install oracle 19.0.1
\n  jjvmm remove --cache --all
\n  jjvmm remove --cache Oracle
\n  jjvmm remove --cache Oracle 19.0.1
\n  jjvmm remove --cache --install Oracle
\n  jjvmm remove --cache --install Oracle 19.0.1
\n  jjvmm remove -i Oracle
\n  jjvmm remove -i oracle 19.0.1
\n  jjvmm remove -c -a
\n  jjvmm remove -c Oracle
\n  jjvmm remove -c Oracle 19.0.1
\n  jjvmm remove -c -i Oracle
\n  jjvmm remove -c -i Oracle 19.0.1
""",
            short_help="Remove cached or installed Java environment.",
            params=[
                RemoveCommandCacheOption(
                    param_decls=("--install",),
                    is_flag=True,
                    help="Only delete installed Java."
                )
                # RemoveCommandallOption(),
                # RemoveCommandInstallOption(),
                # RemoveCommandPublisherArgument(),
                # RemoveCommandVersionArgument()
            ]
        ))

        VMFJ.vmfj()


if __name__ == '__main__':
    pass
