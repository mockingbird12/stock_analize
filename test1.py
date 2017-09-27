# -*- coding: utf-8 -*-

from grab import Grab
import json
import time
from my_functions import *
# import matplotlib.pyplot as plt


#########################################################
# JSON:
#       'c' - ? close закрытие
#       'scale'
#       'h' - high  наивысшая цена
#       'l' - low   самая низкая цена
#       'o' - ? open
#       's'
#       't' - time время
###########################################################

# v 1. перевод желаемой даты в unix-time
# 2. подсчет портфеля на данный момент
#   v список все бумаг
#   v количество по кажой бумаге
#   v подсчет всей суммы
# 3. Статистические операции

tickers = {'GMKN':12, 'AFLT':600, 'AFKS':3700, 'MFON':120, 'YNDX':50, 'MOEX':540, 'FEES':320000, 'UPRO':17000, 'RTKM':350, 'SBERP':200}


def set_time_interval():
    year = 2017
    month = 8
    day = 25
    hour = 10
    minute = 00
    second = 00
    w_day = 0 # по английскому исчислению
    y_day = 0 # день в году
    dl_save = 0 # не обязательные параметры
    start_date = (year, month, day, hour, minute, second, w_day, y_day, dl_save)
    return time.mktime(start_date)


def get_data_from_bcs(ticket):
    bcs_url = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol=' + ticket + '&resolution=60&from=' + start_date + '&to=' + stop_date + '&token=&_='+stop_date
    print bcs_url
    agent_linux = 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'
    g1 = Grab(log_dir=".", user_agent=agent_linux, reuse_cookies=True,
              cookies={'ASP.NET_SessionId':'gi3xsh2e3yyqfycw5mu14keu'}, debug=True)
    g1.go(bcs_url)
    print (g1.response.body)


def get_current_state(start_date, stop_date):
    # total_cache = 0
    # f1 = open('report.txt', 'a')
    for ticket in tickers.keys():
        get_data_from_bcs(ticket)
        print ticket
        # stock_analize(data_json)
        # tmp_summ = tickers.get(ticket) * data_json['c'][len(data_json['c']) - 1]
        # f1.write(ticket)
        # f1.write("Сумма закрытия - " + str(data_json['c'][len(data_json['c']) - 1]) + '\n')
        # f1.write("Сумма по бумаге - " + str(tmp_summ)+'\n')
        # total_cache += float(tmp_summ)
        # print total_cache
        time.sleep(2)
    # f1.write("Общая стоимость портфеля: ")
    # f1.write(str(total_cache))




# plt.grid(True)

start_date = str(set_time_interval())[:-2]
stop_date = str(time.time())[:-3]
print ("stop_date", stop_date)
get_current_state(start_date, stop_date)

# for ticket in tickers.keys():
#     bcs_url = 'http://api.bcs.ru/udfdatafeed/v1/history?symbol=' + ticket + '&resolution=60&from=' + start_date + '&to=' + stop_date + '&token=&_=1490528109299'
#     g1 = Grab(log_file='grab.log', connect_timeout=15)
#     g1.go(bcs_url)
#     print ticket
#     summ_by_ticket(json.loads(g1.response.body))
#     time.sleep(5)

# for i in ['c', 'l', 'h', 'o']:
#     # data_float = [float(item) for item in data_json[i]]
#     print ('\t'+i)
#     print ('\t',data_json[i][len(data_json[i])-1])
# print ()

#         plt.plot(data_float)
# plt.show()