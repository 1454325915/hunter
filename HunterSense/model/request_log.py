#!/ usr/bin/env
# coding=utf-8
#
# Copyright 2019 ztosec & https://www.zto.com/
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
author: b5mali4
"""
import time
import datetime
from peewee import *
from .base_model import BaseModel
from .base_model import BaseModelService
from common.sqllite_util import SqliteManage


class RequestLog(BaseModel):
    """
    To Create Table:
    >>> if __name__ == "__main__":
    >>>     RequestLog.create_table()
    
    ip : 目标IP
    port: 目标端口
    protocol: 协议
    time: 时间
    plugin: 插件名称
    recv_data: 原始请求数据
    time_stamp: 时间戳
    """
    ip = TextField(default='')
    port = TextField(default='')
    protocol = TextField(null=True)
    time_str = DateTimeField(formats='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)
    plugin = TextField(default='')
    recv_data = TextField(default='')
    time_stamp = FloatField(null=True, default=time.mktime(datetime.datetime.now().timetuple()))

    class Meta:
        database = SqliteManage.get_database()


class RequestLogService:
    @staticmethod
    def get_fields_by_where(**kwargs):
        """
        To use:
        >>> request_logs = RequestLogService.get_fields_by_where(fields=(RequestLog.port, RequestLog.plugin), where=(RequestLog.protocol == 'udp'))
        >>> print(request_logs)
        :param kwargs: 
        :return: 
        """
        return BaseModelService.get_fields_by_where(RequestLog, **kwargs)

    @staticmethod
    def remove(**kwargs):
        """
        数据库删除操作
        To use:
        >>> RequestLogService.remove(where=(RequestLog.id == 26))
        :param kwargs: 
        :return: 
        """
        return BaseModelService.remove(RequestLog, **kwargs)

    @staticmethod
    def count(**kwargs):
        """
        数据数量
        To use:
        >>> RequestLogService.count(where=(RequestLog.id == 26))
        :param kwargs: 
        :return: 
        """
        return BaseModelService.count(RequestLog, **kwargs)

    @staticmethod
    def update(**kwargs):
        """
        更新操作
        To use:
        >>> RequestLogService.update(fields=({RequestLog.port: "7998" }))
        :param kwargs: 
        :return: 
        """
        return BaseModelService.update(RequestLog, **kwargs)

    @staticmethod
    def save(**kwargs):
        """
        更新操作
        To use:
        >>> RequestLogService.save(ip="127.0.0.1")
        :param kwargs: 
        :return: 
        """
        return BaseModelService.save(RequestLog, **kwargs)
