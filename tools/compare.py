# -*- coding:utf-8 -*-
# @Time : 2020/7/30 下午5:44
# @Author: hang.yu06
# @File : compare.py


if __name__ == '__main__':
	a = [100079018, 100072007, 100077006, 100000291, 100000178, 100079033, 123000092, 100001038, 100073001,
		 100075002, 100001087, 100000229, 100000029, 100017003, 100000076, 100079003, 100000153, 100003002,
		 100000109, 100000086, 100000129, 100073009, 100000025, 100000105, 100000102, 100000121, 100000096,
		 100000170, 100001061, 100001009, 100001050, 100001073, 100001016, 100000106, 100001067, 100001007,
		 100019005, 100000097, 100000062, 100079012, 100077005, 100000075, 100001128, 100079022, 100000090,
		 100000031, 100000069, 100000133, 100001029, 100003001, 100001001, 100000023, 100001123, 100001028,
		 100025002, 100005002, 100003006, 100001013, 100006001, 100000081, 100000237, 100001076, 100000111,
		 100073008, 100000298, 100079010, 100001125, 100002006, 100077002, 100000088, 100079021, 100001107,
		 100000158, 100000181, 100071005, 100001090, 100010002, 100000089, 100006003, 100006002, 100000112,
		 100071003, 100001088, 100001086, 100001062, 100016003, 100000238, 100027001, 100000221, 100001106,
		 100000063, 100001002, 100000067, 100000082, 100016002, 100000162, 100000056, 100000103, 100000085,
		 100001108, 100000027, 100000152, 100001092, 100000018, 100001019, 100076009, 100016001, 123001059,
		 123001035, 123000013, 123001061, 123000081, 123000020, 123000079, 123001018, 123000012, 123001022,
		 123000022, 123000082, 123001028, 123001003, 123001050, 123000030, 123000033, 123000019, 123000161,
		 123001037, 123001057, 123000060, 123001062, 123000038, 123001038, 123000032, 123001012, 123001029,
		 123001080, 123001033, 123000056, 123000007, 123001013, 123000170, 123001030, 123000015, 123001025,
		 100000287, 100011007, 100008001, 100008003, 123000150, 100000005]
	b = [100010002, 100005002, 100001001, 100001002, 100001003, 100001005, 100001006, 100001007, 100019002, 100006002,
		 100006001, 100016001, 100016002, 100003001, 100003003, 100003002, 100017002, 100002001, 100002002, 100003005,
		 100000696, 100000632, 100000631, 100000630, 100000629, 100000628, 100000627, 100000626, 100000625, 100000623,
		 100000622]

	for i in b:
		if i not in a:
			print(i)
