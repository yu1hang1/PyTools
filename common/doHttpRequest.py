# -*- coding:utf-8 -*-
# @Time : 2020/8/6 下午6:32
# @Author: hang.yu06
# @File : doHttpRequest.py
import json
import logging

import requests
from pycookiecheat import chrome_cookies


class HttpRequestHandel(object):

	def doRequset(self, url=None, request_method=None, param=None):
		try:
			cookies = chrome_cookies(url)
			resp = None
			if request_method == "POST":
				resp = requests.post(url=url, headers=cookies, json=param)
			if request_method == "GET":
				resp = requests.get(url=url, headers=cookies, params=param)
			result = json.loads(resp.content.decode()) if resp.status_code == 200 else {}
			return result
		except Exception as e:
			logging.error(e)
			return 0


HttpRequestHandel = HttpRequestHandel()
