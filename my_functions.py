# -*- coding: utf-8 -*-
import time


def stock_analize(stock_data):
    i = 0
    day_count = 0
    price = []
    day_data = []
    price_differ = []
    for unix_date in stock_data['t']:
        day_count += 1
        if day_count == 9:
            day_data.append(time.ctime(unix_date)[4:10])
            price.append(stock_data['c'][i])
            day_count = 0
        i += 1
    print day_data
    print stock_data['c']
    # f1 = open('stock_analize','a')
    # for day in day_data: f1.write("%10s\t" % day)
    # f1.write('\n')
    # for j in price: f1.write("%f\t" % j)
    # f1.write('\n')
    # for i in range(0, len(price) - 1): price_differ.append(price[i+1] - price[i])
    # for k in price_differ: f1.write("%f\t" % k)
    # f1.write('\n''\n')
    # return None


def summ_by_ticket(data_json):
    total_summ = 0
    for i in data_json['o']:
        total_summ += float(i)
    result = total_summ / len(data_json['o'])
    print result