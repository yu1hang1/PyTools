# -*- coding:utf-8 -*-
# @Time : 2020/8/24 下午5:21
# @Author: hang.yu06
# @File : dubbo_admin_filter.py
from common.doHttpRequest import HttpRequestHandel
import re

request_method = 'GET'
prod_headers = {
	'Cookie': 'operator_ticket=69bc6fa412c0424ab26e4f8d15624373; operator_sign=a61c5c1c0fe50ee6f227fe7d7838f46f; operator_timestamp=1598233820068; user_name=hang.yu06'}
prod_param = {}
prod_url = 'https://dubbo-admin.corp.bianlifeng.com/api/dev/services'

services = HttpRequestHandel.doRequset(prod_url, request_method, prod_headers, prod_param)
new_services = []
greedy_pattern= re.compile(r'.*/com.opc.display')
for i in services:
	if "gray" not in i and "/com.opc.display" in i:
		j =greedy_pattern.match(i)
		if "com.opc.display.api" not in j.group():
			new_services.append(j.group())
			print(j.group())

if __name__ == "__main__":
	pass
