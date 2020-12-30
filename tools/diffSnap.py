# -*- coding:utf-8 -*-
# @Time : 2020/8/6 下午6:29
# @Author: hang.yu06
# @File : diffSnap.py
import json
import json_tools
import requests

from common.doHttpRequest import HttpRequestHandel


def doRequest():
	headers = {
		'Cookie': 'chenlie-gray:g=; operator_ticket=3a14f4467ee84ef2bc2de83b17cf13cb; operator_sign=8cce69c2426b685895ef6aa784b8142b; operator_timestamp=1596765919837; user_name=hang.yu06'}
	dailaySnapID = {"snapId": 4332724}
	unDailySanpID = {"snapId": 4332722}
	url = 'https://display-gray.corp.bianlifeng.com/chenlie/api/core/v3/queryShopSnapById'
	request_methode = 'GET'
	dailaySnap = HttpRequestHandel.doRequset(url, request_methode, headers, dailaySnapID)
	unDailySanp = HttpRequestHandel.doRequset(url, request_methode, headers, unDailySanpID)
	dailaySnap = dailaySnap.get("snap")
	unDailySanp = unDailySanp.get("snap")

	DailaySnap_9 = {}
	for k, v in dailaySnap.items():
		newShelf = ShelfFilter(v)
		if ShelfFilter(v):
			DailaySnap_9[k] = ShelfFilter(newShelf)

	unDailySanp_9 = {}
	for k, v in unDailySanp.items():
		newShelf = ShelfFilter(v)
		if ShelfFilter(v):
			unDailySanp_9[k] = ShelfFilter(newShelf)
	print(f'DailaySnap_9长度{len(DailaySnap_9)}')
	print(f'DailaySnap_9{DailaySnap_9}')
	print(f'unDailySanp_9长度{len(unDailySanp_9)}')
	print(f'unDailaySnap_9{unDailySanp_9}')
	diffResult = json_tools.diff(dailaySnap, unDailySanp_9)
	print(diffResult)


def ShelfFilter(shelf):
	newShelf = []
	for level in shelf:
		if level.get("useId") == 9:
			newShelf.append(level)
	return newShelf


if __name__ == "__main__":
	doRequest()
