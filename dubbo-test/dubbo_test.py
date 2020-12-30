# -*- coding:utf-8 -*-
# @Time : 2020/4/9 下午10:28
# @Author: hang.yu06
# @File : dubbo_test.py
import dubbo_telnet


def dubbo_test():
	host = "10.225.187.20"
	port = 20881
	conn = dubbo_telnet.connect(host, port)

	# 设置telnet连接超时时间
	conn.set_connect_timeout(500)

	# 设置dubbo服务返回响应的编码
	conn.set_encoding('gbk')
	interface = "com.opc.display.api.remote.AttachedShelfRemote"
	method = "queryAttachedShelfLocationByShopLayoutId"
	print(conn.invoke(interface, method, 139664))

	# command = 'invoke com.opc.display.api.remote.AttachedShelfRemote.queryAttachedShelfLocationByShopLayoutId(139664)'
	#
	# conn.do(command)


if __name__ == "__main__":
	# 设置telnet连接超时时间
	dubbo_test()
	interface = 'com.zrj.pay.trade.api.QueryTradeService'
	method = 'tradeDetailQuery'
	param = '{"id": "nimeide"}'

	command = 'invoke com.zrj.pay.trade.api.QueryTradeService.tradeDetailQuery({"id":"nimeide"})'
