# -*- coding: utf-8 -*-

import urllib
import json
import datetime
from my_functions import *
import numpy
import matplotlib.pyplot as plt


class MyPlot():

    def __init__(self, title_name, data):
        super.__init__()
        self.grid(True)
        self.plot.title(title_name)
        self.plot.plot(data)

    def show(self):
        self.plot.show()



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

extra_index = ['MICEXINDEXCF', 'BRENT', 'USD000000TOD']
tickers = {'GMKN':12, 'AFLT':600, 'AFKS':3700, 'MFON':120, 'YNDX':50, 'MOEX':540, 'FEES':320000, 'UPRO':17000, 'RTKM':350, 'SBERP':200}


def plot_graf(cur_data, name, dates):
    dates_text = str(datetime.datetime.fromtimestamp(float(dates[0]))) + " - " + str(datetime.datetime.fromtimestamp(float(dates[1])))
    working_array_cur = numpy.array(cur_data['o'])
    # working_array_etalon = numpy.array(etalon_data['o'])
    max_val = [working_array_cur.max()] * len(cur_data['o'])
    min_val = [working_array_cur.min()] * len(cur_data['o'])
    working_array_cur = working_array_cur / working_array_cur.max()
    # working_array_etalon = working_array_etalon / working_array_etalon.max()
    plt.title(name)
    plt.plot(working_array_cur.tolist())
    # plt.plot(working_array_etalon.tolist())
    # plt.plot(max_val)
    # plt.plot(min_val)
    plt.text(len(cur_data['o']) / 2, max_val[0], max_val[0])
    plt.text(len(cur_data['o']) / 2, min_val[0], min_val[-1])
    plt.xlabel(dates_text)
    plt.ylabel(u'Стоимость')
    plt.grid(True)
    plt.show()


def plot_income():

    pass


def set_time_interval():
    hours = 24
    days = 30
    stop_date = int(time.mktime(time.localtime()))
    start_date = stop_date - (3600 * hours * days)
    return str(start_date), str(stop_date)


def get_data_from_bcs(ticket, dates):
    start_date = dates[0]
    stop_date = dates[1]
    bcs_url = 'https://api.bcs.ru/udfdatafeed/v1/history?symbol=' + ticket + \
              '&resolution=60&from=' + start_date + '&to=' + stop_date + '&token=&_='+stop_date
    print (bcs_url)
    raw_data = urllib.urlopen(bcs_url)
    data_array = json.load(raw_data)
    return data_array


def get_current_income():
    dates = [set_time_interval()]
    for ticket in tickers.keys():
        print (ticket)
        data_json = get_data_from_bcs(ticket, dates)
        price_list = data_json['o']
        total_cache = [price * tickers.get(ticket) for price in price_list]
        # my_plot = MyPlot(ticket, total_cache)
        # my_plot.show()


def get_current_state():
    start_date, stop_date = set_time_interval()
    dates = [start_date, stop_date]
    micex_json = get_data_from_bcs('USD000000TOD', dates)
    for ticket in tickers.keys():
        print (ticket)
        data_json = get_data_from_bcs(ticket, dates)
        plot_graf(data_json, ticket, dates)
        average_annual(data_json['c'])
        dispersion(data_json['c'])
        # stock_analize(data_json)
        time.sleep(2)


get_current_state()
# get_current_income()
