#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 2020-12-02 15:42
import json

from datetime import datetime
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 cdn 产品模块的 models
from tencentcloud.cdn.v20180606 import models

from api.get_client_profile import get_client_instance

def get_cdn_client_instance(id, key):
    '''获取cdn的实例，用于后面对cdn的各种操作
    '''
    client = get_client_instance(id, key, "cdn")
    return client


def get_cdn_url_push_info(client):
    '''查询CDN预热配额和每日可用量
    '''
    try:
        req = models.DescribePushQuotaRequest()
        params = {}
        req.from_json_string(json.dumps(params))
        resp = client.DescribePushQuota(req)
        # print(resp.to_json_string())
        print("获取CDN预热配额和每日可用量信息成功")
        return resp.UrlPush

    except TencentCloudSDKException as err:
        print(err)
        return []


def update_cdn_url_push(client, urls):
    '''指定 URL 资源列表加载至 CDN 节点，支持指定加速区域预热
    默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 20 条
    '''
    try:
        req = models.PushUrlsCacheRequest()
        params = {
            "Urls": urls
        }
        req.from_json_string(json.dumps(params))
        resp = client.PushUrlsCache(req)
        print(resp.to_json_string())
        print("URL:{}预热成功".format(', '.join(urls)))
        return True

    except TencentCloudSDKException as err:
        print(err)
        return False
