#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
import random

if __name__ == '__main__':
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
print("定时预约抢购...")
sku_id = '100012043978'
asst.print_item_info(sku_id)
reserve_info = asst.get_reserve_info(sku_id)
reserve_time = reserve_info.get("yueStime")
buy_time = reserve_info.get("qiangStime")
print("预约时间:",reserve_time)
print("抢购时间:",buy_time)
# 开始预约
if reserve_time :
    asst.make_reserve(sku_id, reserve_time + '.000')
else:
    print('获取预约时间失败')
# 开始抢购
if buy_time :
    rand_msecond = random.randint(1,9) * 1000
    buy_time = buy_time + '.000'
    #buy_time = buy_time + "." + str(rand_msecond)
else:
    print('获取抢购时间失败')
    buy_time = input("请输入抢购时间(2020-03-04 00:59:59.000):")
#asst.exec_reserve_seckill_by_time(sku_id=sku_id,buy_time=time, retry=10, interval=1,num=1)
asst.exec_seckill_by_time(sku_ids=sku_id,buy_time=buy_time, retry=15, interval=0.2,num=2)
