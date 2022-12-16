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
        添加子命令，实现命令行参数、选项、帮助信息
        :return:无
        """
        # 通过命令行组的add_command方法创建remove子命令

        VMFJ.vmfj.add_command(cmd=RemoveCommand(
            # 子命令名称
            name="remove",
            # 帮助与信息
            help="""
this is remove command 
\nfor example:
\n\txxx
\ndelete all Java JDK use:
\n\tvmfj remove all
\n\tvmj remove -i/--install all
\n\tvmfj remove -c/--cache all
\n\tvmfj remove -i -c/--install-cache all
\n\tvmfj remove -c -i/--cache-install all
""",
            # 短帮助信息
            short_help="Remove cached or installed Java environment.",
            # 参数（包含选项和参数）
            params=[
                # 自定义选项类
                RemoveCommandInstallOption(
                    # 选项名称
                    param_decls=("-i", "--install"),
                    is_flag=True,
                    help="Only delete installed Java."
                ),
                RemoveCommandallOption(
                    param_decls=("-i", "-c", "--install", "--cache"),
                    is_flag=True,
                    help="Delete all Installed and Cache."
                ),
                RemoveCommandCacheOption(
                    param_decls=['-c', '--cache'],
                    is_flag=True,
                    help="Only delete Cache Java"
                ),
                RemoveCommandPublisherArgument(
                    param_decls=["publisher"],
                    required=False
                ),
                RemoveCommandVersionArgument(
                    param_decls=["version"],
                    required=False
                )
            ]
        ))

        VMFJ.vmfj.add_command(cmd=DoctorCommand(
            name="doctor",
            help="this is dockor.",
            params=[
                DoctorCommandFixOption(
                    param_decls=("-f", "--fix"),
                    is_flag=True,
                    help="Fix environment variable"
                )
            ]
        ))

        VMFJ.vmfj.add_command(cmd=ListCommand(
            name="list",
            help="this is list",
            params=[
                ListCommandPublisherArgument(
                    param_decls=["publisher"],
                    required=False,
                    default="all"
                )
            ]
        ))

        VMFJ.vmfj.add_command(cmd=InstallCommand(
            name="install",
            help="this is install",
            params=[
                InstallCommandDownloadOnlyOption(
                    param_decls=("--download-only", "-o"),
                    is_flag=True,
                    help="this is install"
                ),
                InstallCommandPublisherArgument(
                    param_decls=["publisher"],
                    required=False
                ),
                InstallCommandVersionArgument(
                    param_decls=["version"],
                    required=False
                )
            ]
        ))

        VMFJ.vmfj.add_command(UseCommand(
            name="use",
            help="this is use.",
            params=[
                UseCommandPublisherArgument(
                    param_decls=["publisher"],
                    required=False
                ),
                UseCommandVersionArgument(
                    param_decls=["version"],
                    required=False
                )
            ]
        ))

        VMFJ.vmfj()


if __name__ == '__main__':
    pass
