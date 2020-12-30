# -*- coding:utf-8 -*-
# @Time : 2020/7/22 下午9:20
# @Author: hang.yu06
# @File : syncWconfig.py

from common.doHttpRequest import HttpRequestHandel


def syncWconfig():
	# 0、指定appCode
	appCode = 'w_idss_display_post'

	# 1、线上FileId
	request_method = 'GET'
	prod_param = {'appName': appCode, 'profile': 'prod'}
	prod_url = 'https://fd.corp.bianlifeng.com/wconfig/admin/config/list_configs/v1'
	prod_dataIds = []
	prod_Reponse = HttpRequestHandel.doRequset(prod_url, request_method, prod_param)
	for prod_data in prod_Reponse.get('data'):
		prod_dataIds.append(prod_data.get('dataId'))
	print(f'线上环境app的wconfig文件：{prod_dataIds}')

	# 2、线下FileId
	beta_param = {'appName': appCode, 'profile': 'beta'}
	beta_url = 'http://fd.beta.wormpex.com/wconfig/admin/config/list_configs/v1'
	beta_dataIds = []
	beta_Reponse = HttpRequestHandel.doRequset(beta_url, request_method, beta_param)
	for beta_data in beta_Reponse.get('data'):
		beta_dataIds.append(beta_data.get('dataId'))
	print(f'测试环境wconfig文件：{prod_dataIds}')
	print(f'差异值：{list(set(prod_dataIds).difference(set(beta_dataIds)))}')


if __name__ == "__main__":
	syncWconfig()
