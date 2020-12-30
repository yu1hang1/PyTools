# -*- coding: utf-8 -*-
from imp import reload
from math import ceil
import time
import os

### 根据需要，修改数据库名称
database = 'idss_ims_instruction'
import platform

pyVersion = platform.python_version()[0:1]
print("当前python版本是" + pyVersion)
if pyVersion == "3":
	import pymysql

	conn = pymysql.connect(host="biz1-w-mysql.beta.vip.wormpex.com", port=33007, user="dev",
						   password="096667f9c7d0396d", database="qa_database_operation", charset="utf8")
else:
	import MySQLdb

	conn = MySQLdb.connect(
		host='biz1-w-mysql.beta.vip.wormpex.com',
		port=33007,
		user='dev',
		passwd='096667f9c7d0396d',
		db='qa_database_operation',
	)
conn.autocommit(True)
cur = conn.cursor()

# --------------------------------------------
# 以下代码，解决string格式化时候，ascii码不能超过128位的问题
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
	reload(sys)
	sys.setdefaultencoding(defaultencoding)
# ------------------------------------------------

file_name = database + '.sh'
import logging

logging.basicConfig(level=logging.INFO, filename=file_name, filemode='w', format="%(message)s")

header = '''#! /bin/sh

function func_log_print()
{
        local level="$1"
        local msg="$2"
        case $level in
                error)
                        echo -e "${msg}"
                        ;;
                info)   echo -e "${msg}"
                        ;;
                *)      echo "${msg}";;
        esac
}

function check_exec_status()
{
        if [ $? -eq 0 ];then
                func_log_print "info" "success"
        else
                func_log_print "error" "fail"
        fi
}'''

logging.info(header)

sql = "SELECT  `beta_dump_tables`.*,`beta_dump_datasource`.`host`,`beta_dump_datasource`.`port` FROM `beta_dump_tables` LEFT OUTER JOIN `beta_dump_datasource` ON `beta_dump_datasource`.`database_name` = `beta_dump_tables`.`database_name` WHERE `beta_dump_tables`.`database_name` = '%s'" % (
	database)
cur.execute(sql)


def check_empty(string):
	if string is None or string == '':
		return True
	return False


def join_and_bracket(list):
	joins = ",".join(list)
	return "( " + joins + " )"


def get_data(string):
	return time.strftime(string, time.localtime(time.time()))


mysql_pwd_str = 'mysql --defaults-file=/etc/sync_beta.cnf'
mysql_dump_pwd_str = 'mysqldump --defaults-file=/etc/sync_beta.cnf'
# mysql_pwd_str = "mysqldump -u'dumper' -p'0af8e1188112d1a4'"
logging.info("echo  -e  '检查线下库是否存在'")
logging.info("%s -h datamask1-w-mysql.beta.vip.wormpex.com -P 33007 -e 'CREATE DATABASE IF NOT EXISTS  %s'" % (
	mysql_pwd_str, database))
logging.info("check_exec_status")
for i in cur.fetchall():
	database_name = i[1]  ## db名称
	dump_table = i[2]  ##
	partition_format = i[3]  ## 分表参数
	in_field = i[4]  ## 可能为空
	in_clause = i[5]  ##  in_field 跟随上面
	time_filter = i[6]  # 可能空
	time_slice = i[7]  # 跟随上面
	host = i[10]
	port = i[11]
	re = []
	#   store_file_prefix = '~/'
	store_file_prefix = '/data/dump/'
	if not check_empty(partition_format):
		dump_table = dump_table.replace("{data}", get_data(partition_format), 100)
	# 都为空的情况
	if check_empty(in_field) and check_empty(time_filter):
		sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s > %s%s.%s.sql  2>/dev/null' % (
			mysql_dump_pwd_str, host, port, database_name, dump_table, store_file_prefix, database_name, dump_table)
		re.append(sql)
	# infield不为空情况
	elif not check_empty(in_field) and not check_empty(in_clause) and check_empty(time_filter):
		codelist = in_field.replace("(", '').replace(")", '').split(',')
		list_len = len(codelist)
		single_num = 100
		sql_num = ceil(list_len / single_num * 1.0)
		if sql_num >= 2:
			logging.info("echo 'dba的dump条件限制长度，拆分为 %d 条sql dump'" % (sql_num))
			for i in range(1, sql_num + 1):
				if i == 1:
					in_clause = join_and_bracket(codelist[(i - 1) * single_num: i * single_num])
					sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s --where="%s in %s" > %s%s.%s.sql 2>/dev/null' % (
						mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause,
						store_file_prefix,
						database_name, dump_table)
					re.append(sql)
				else:
					in_clause = join_and_bracket(codelist[(i - 1) * single_num: i * single_num])
					sql = '%s --single-transaction --set-gtid-purged=off --skip-add-drop-table --no-create-info  -h %s -P %s %s %s --where="%s in %s" >> %s%s.%s.sql 2>/dev/null' % (
						mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause,
						store_file_prefix,
						database_name, dump_table)
					re.append(sql)
		else:
			sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s --where="%s in %s" > %s%s.%s.sql 2>/dev/null' % (
				mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause, store_file_prefix,
				database_name,
				dump_table)
			re.append(sql)
	elif check_empty(in_field) and not check_empty(time_slice) and not check_empty(time_filter):
		sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s --where="%s >= curdate() - interval %s day " > %s%s.%s.sql 2>/dev/null' % (
			mysql_dump_pwd_str, host, port, database_name, dump_table, time_filter, time_slice, store_file_prefix,
			database_name, dump_table)
		re.append(sql)
	# 都不为空情况
	elif not check_empty(in_field) and not check_empty(in_clause) and not check_empty(time_filter) and not check_empty(
			time_slice):
		codelist = in_clause.replace("(", '').replace(")", '').split(',')
		list_len = len(codelist)
		single_num = 100
		sql_num = ceil(list_len / (single_num * 1.0)).__int__()
		if sql_num >= 2:
			logging.info("echo 'dba的dump条件限制长度，拆分为 %d 条sql dump'" % (sql_num))
			for i in range(1, sql_num + 1):
				if i == 1:
					in_clause = join_and_bracket(codelist[(i - 1) * single_num:  i * single_num])
					sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s --where="%s in %s and %s >= curdate() - interval %s day " > %s%s.%s.sql 2>/dev/null' % (
						mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause, time_filter,
						time_slice,
						store_file_prefix, database_name, dump_table)
					re.append(sql)
				else:
					in_clause = join_and_bracket(codelist[(i - 1) * single_num: i * single_num])
					sql = '%s --single-transaction --set-gtid-purged=off --skip-add-drop-table --no-create-info  -h %s -P %s %s %s --where="%s in %s and %s >= curdate() - interval %s day " >> %s%s.%s.sql 2>/dev/null' % (
						mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause, time_filter,
						time_slice,
						store_file_prefix, database_name, dump_table)
					re.append(sql)
		else:
			sql = '%s --single-transaction --set-gtid-purged=off -h %s -P %s %s %s --where="%s in %s and %s >= curdate() - interval %s day " > %s%s.%s.sql 2>/dev/null' % (
				mysql_dump_pwd_str, host, port, database_name, dump_table, in_field, in_clause, time_filter, time_slice,
				store_file_prefix, database_name, dump_table)
			re.append(sql)
	else:
		logging.info("有错误数据")
	logging.info("echo  -e  '\\n'")
	logging.info("func_log_logging.info'info' '%s'" % ("开始导出表：" + dump_table))
	for s in re:
		logging.info(s)
		logging.info("check_exec_status")
	logging.info("echo 文件%s%s.%s.sql大小是：$(du -sh  %s%s.%s.sql | awk '{logging.info$1}') " % (
		store_file_prefix, database_name, dump_table, store_file_prefix, database_name, dump_table))
	logging.info("echo  -e '开始导入表'")
	logging.info(
		"mysql --defaults-file=/etc/sync_beta.cnf -h datamask1-w-mysql.beta.vip.wormpex.com -P 33007  %s < %s%s.%s.sql" % (
			database_name, store_file_prefix, database_name, dump_table))
	logging.info("check_exec_status")
logging.info("echo -e '清除临时文件'")
logging.info("rm -rf %s%s.*.sql" % (store_file_prefix, database))
