# -*- coding: utf-8 -*-

import urllib
import json
import datetime
from my_functions import *
import numpy
import matplotlib.pyplot as plt


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


def plot_graf(data, name, dates):
    dates_text = str(datetime.datetime.fromtimestamp(float(dates[0]))) + " - " + str(datetime.datetime.fromtimestamp(float(dates[1])))
    working_array = numpy.array(data['o'])
    max_val = [working_array.max()] * len(data['o'])
    min_val = [working_array.min()] * len(data['o'])
    plt.title(name)
    plt.plot(data['o'])
    plt.plot(max_val)
    plt.plot(min_val)
    x_text = len(data['o'])
    y_text = float(data['o'][-1])
    # plt.text(x_text, y_text, dates_text)
    plt.text(len(data['o'])/2, max_val[0], max_val[0])
    plt.text(len(data['o'])/2, min_val[0], min_val[-1])
    plt.xlabel(dates_text)
    plt.ylabel(u'Стоимость')
    plt.grid(True)
    plt.show()


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


def get_data_from_bcs(ticket, dates):
    start_date = dates[0]
    stop_date = dates[1]
    bcs_url = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol=' + ticket + \
              '&resolution=60&from=' + start_date + '&to=' + stop_date + '&token=&_='+stop_date
    print (bcs_url)
    raw_data = urllib.urlopen(bcs_url)
    data_array = json.load(raw_data)
    return data_array


def get_current_state():
    start_date = str(set_time_interval())[:-2]
    stop_date = str(time.time())[:-3]
    dates = [start_date, stop_date]
    for ticket in tickers.keys():
        print (ticket)
        data_json = get_data_from_bcs(ticket, dates)
        plot_graf(data_json, ticket, dates)
        average_annual(data_json['c'])
        dispersion(data_json['c'])
        # stock_analize(data_json)
        time.sleep(2)



get_current_state()
