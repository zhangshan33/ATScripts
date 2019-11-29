# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

请求相关
'''

import json
import requests
from bs4 import BeautifulSoup
from uti.LoggerHandler import logger


class RequestHandler(object):

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response = self.send_request()
        return response

    def send_request(self):
        """ 发请求 """
        try:
            response = requests.request(
                method=self.case['case_method'],
                url=self.case['case_url'],
                params=self._check_params()
            )
            content_type = response.headers['Content-Type']
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                response = getattr(self, '_check_{}_response'.format(content_type))(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']

        return response

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
        else:  # 执行成功
            logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
            return {key: self.case_expect[key]}, {key: response[key]}

    def _check_html_response(self, response):
        """ 校验html类型的数据"""
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        title = soup_obj.find('title').text
        return title, self.case_expect

    def _check_params(self):
        """ 整理参数 """
        if self.case['case_params']:
            """
            做扩展
            """
            pass
        else:
            return {}
