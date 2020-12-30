# -*- coding:utf-8 -*-
# @Time : 2020/5/18 下午5:24
# @Author: hang.yu06
# @File : fileHandeler.py
import json
import os
import sys
import requests
import json_tools

false = False
true = True
null = None


def handel():
	f1 = open("/Users/bianlifeng/Desktop/100005002")
	down = f1.read()
	down = eval(down)
	print()
	f1.close()

	cookie = "operator_ticket=5700433f749943ea977953d195a10e8d; user_name=hang.yu06; operator_sign=ee2afc7305dc49933be7af6864d0cc96; operator_timestamp=1590657766200"
	param = {"shopCode": "100005002", "snapId": "3489562"}
	resp = requests.get(url="http://b1.opc.beta.wormpex.com/chenlie/api/auto/test/query/strqtegyParam",
						headers={'cookie': cookie}, params=param)

	post = json.loads(resp.content.decode())
	post = post.get("data", None)

	try:
		report = __diffResp(down, post)
		report = str(report)
		print(report)
		f3 = open("/Users/bianlifeng/Desktop/diffResult", "w")
		f3.write(report)
		f3.close()
		return "success"
	except Exception as e:
		print(e)
		return "fail"


def __diffResp(old_result, new_result):
	diff_result = json_tools.diff(old_result, new_result)
	return {
		"diff_result": diff_result,
	}


if __name__ == "__main__":
	pass
