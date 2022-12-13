#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import platform
import os
import getpass
import configparser

from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.util.string_util import StringUtil
from libcore.exception.not_support_system_type_exception import Notsupportsystemtypeexception
from libcore.exception.get_system_info_exception import Getsysteminfoexception
from libcore.exception.config_file_parse_failed_exception import ConfigFileParseFailedException
from libcore.exception.config_value_not_exist_exception import ConfigValueNotExistException


class Config:
    """
    配置类
    """

    __default_mirror = None
    __default_lang = "en_US"
    __default_publisher = "Oracle"

    __config_file_windows_tpl = "{system_root}\\Users\\{username}\\AppDate\\Local\\vmfj\\config\\.vmfj-config.ini"
    __config_file_osx_tpl = "/User/{username}/.vmfj/Config/.vmfj-config.ini"
    __config_file_linux_tpl = "/home/{username}/.vmfj/config/.vmfj-config.ini"

    __config_file_windows = None
    __config_file_osx = None
    __config_file_linux = None

    __curr_system_type = None
    __curr_system_name = None
    __curr_windows_system_root = None

    __curr_system_location = None

    __config_file = None

    __key = None

    __allow_config_keys = (
        "mirror",
        "lang",
        "publisher"
    )

    def __init_system_info(self):
        """
        获取操作系统各种信息
        :return:
        """
        system_type = platform.system()
        curr_username = getpass.getuser()
        if StringUtil.is_empty(curr_username):
            raise Getsysteminfoexception("Failed to get current user name.")
        self.__curr_system_name = curr_username.strip()

        if system_type == "Darwin":
            self.__curr_system_type = "OSX"

        elif system_type == "Windows":
            system_root = os.getenv("SystemDrive", default="C:")
            if StringUtil.is_empty(system_root):
                raise Getsysteminfoexception("Illegal system root path: {}".format(system_root))
            self.__curr_windows_system_root = system_root.strip()

        elif system_type == "Linux":
            self.__curr_system_type = "Linux"

        else:
            raise Notsupportsystemtypeexception("Unrecognized operating system.")

    def __init_config_file_location(self):
        """
        初始化配置文件路径
        :return:
        """
        if self.__curr_system_type == "OSX":
            self.__curr_system_location = self.__config_file_osx = self.__config_file_osx_tpl.format(curr_username=self.
                                                                                                     __curr_system_name)
        elif self.__curr_system_type == "Windows":
            self.__curr_system_location = self.__config_file_windows = self.__config_file_windows_tpl.format(
                system_root=self.
                __curr_windows_system_root,
                username=self.__curr_system_name)
        elif self.__curr_system_type == "Linux":
            self.__curr_system_location = self.__config_file_linux = self.__config_file_linux_tpl. \
                format(curr_username=self.__curr_system_name)

    def __load_config_file(self):
        """
        加载配置文件
        如果文件不存在，不加载，使用默认的配置参数
        如果第一次保存配置的时候，文件不存在，直接创建。
        如果文件存在，加载，修改。
        :return:
        """
        filename = ""
        if os.path.exists(filename):
            self.__config_file = configparser.ConfigParser()
            self.__config_file.read(filename, encoding="UTF-8")

            if not self.__config_file.has_section("app"):
                raise ConfigFileParseFailedException("Configuration file format error.")

    def __init__(self):
        self.__init_system_info()
        self.__init_config_file_location()
        self.__load_config_file()

    def __err_key(self, key):
        if StringUtil.is_empty(key):
            raise ConfigKeyNotExistException("{}is not in config file, because key is empty".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{}The specified key is illegal.".format(key))

    def get(self, key: str) -> str:
        """
        获取配置项
        :param key: Key
        :return: Value
        """
        key = key.strip()

        self.__err_key(key=key)

        if self.__config_file is None:
            return self.__default_config_key(key)
        else:
            val = self.__config_file.get("app", key).strip()

            # if StringUtil.is_empty(val):
            #     self.__default_config_key(val)
            # return val
            return self.__default_config_key(key) if StringUtil.is_empty(val) else val

    def __default_config_key(self, key: str) -> str:
        if key == "mirror":
            return self.__default_mirror
        elif key == "lang":
            return self.__default_lang
        elif key == "publisher":
            return self.__default_publisher

    def set(self, key: str, value: str) -> bool:
        """
        设置配置项
        :param key: Key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        value = value.strip()
        self.__err_key(key=key)

        if StringUtil.is_empty(value):
            raise ConfigValueNotExistException("{}is not in config file, because key is empty".format(value))
        else:
            self.__config_file.set("app", key, value)
            self.__config_file.write(open(self.__curr_system_location, "w"))
            return True

    def get_with_default(self, key: str, default: str) -> str:
        """
        获取配置项，如果这个配置项的值为空，那么返回用户指定的 default
        :param key: Key
        :return Value
        :param default: 默认值
        :return: Value
        """

        key = key.strip()
        self.__err_key(key=key)

        if StringUtil.is_empty(self.__config_file.get(section="app", option=key)):
            return default
        else:
            return self.__config_file.get(section="app", option=key)


if __name__ == '__main__':
    pass
