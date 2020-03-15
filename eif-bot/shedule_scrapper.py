#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup
import json
import requests
import re
import time
from datetime import datetime, timedelta
import locale  # для русификации дат
import dateutil
import dateutil.parser
import urllib3

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
requests.packages.urllib3.disable_warnings()

links_dict = {
    'ЭиФ': {
        1: 'https://lk.ranepa.ru/schedule/?by=agroup&f=7a410e0c-57b9-11e9-80ed-005056a03e4f',
        2: 'https://lk.ranepa.ru/schedule/?by=agroup&f=52a0a22b-269a-11e8-80ec-000c299441de'
    },
    'СБД': {
        1: 'https://lk.ranepa.ru/schedule/?by=agroup&f=0faf9460-6513-11e9-80f1-005056a03e4f',
        2: 'https://lk.ranepa.ru/schedule/?by=agroup&f=f9fc14ba-2825-11e8-80ec-000c299441de'
    },
    'ПЭ': {
        1: 'https://lk.ranepa.ru/schedule/?by=agroup&f=6e56989d-6513-11e9-80f1-005056a03e4f',
        2: 'https://lk.ranepa.ru/schedule/?by=agroup&f=10d94515-2826-11e8-80ec-000c299441de'
    }
}


class Shedule():

    def __init__(self, prof='ЭиФ', course=1):
        self.link = links_dict[prof][course]

    def next_monday(self, count_week):  # дата понедельника через count_week=1 или 2 недель в формате YYYY-MM-DD
        dt = datetime.now()
        delta = dt.weekday() % 7
        next_monday = (dt + timedelta(days=7 * count_week - delta)).strftime("%Y-%m-%d")
        return (next_monday)  # as datetime object

    def find_replace(self, string, dict_):
        # возвращает string в котором возможные слова из ключей dict меняются на значения dict
        for key in list(dict_.keys()):
            if re.search(key, string) != None:
                string = re.sub(key, dict_[key], string)
        return string

    def shedule_13(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        locale.setlocale(locale.LC_ALL, '');
        shedule_list = []
        i = 0
        k = -2
        while i < 13:
            k += 2
            n_mon = self.next_monday(k)
            base_link = "{}&type=schedule&date=".format(self.link)
            link1 = base_link + n_mon
            while True:
                try:
                    while True:
                        try:
                            html = requests.get(link1, verify=False).content
                            break
                        except:
                            print('Проблема с получением данных от ', link1)
                            time.sleep(30)
                            continue
                    soup = BeautifulSoup(html, 'lxml')
                    shedule = soup.findAll('script', {'type': 'text/javascript'})[-2]  # [16]
                    # print(shedule)
                    p = re.findall('{"days":.*]}', shedule.text)  # re.findall('{"days":.*]}',shedule.text)
                    week_dict = json.loads(p[0])['days'][:-1]  # до следующего воскресенья включительно
                    time.sleep(3)
                    break
                except IndexError:
                    print('IndexError')
                    continue
            for week_day in week_dict:
                if week_day['discs'] == []:
                    continue
                else:
                    if i < 13:
                        i += 1
                        shedule_list.append(week_day)
                    else:
                        break
            if k >= 8:
                break
        return shedule_list

    def shedule_day(self, count_days):
        raspisanie = []
        shedule_13_input = self.shedule_13()
        emoji1 = bytes.decode(b'\xF0\x9F\x93\x86', 'utf8')  # календарь
        emoji2 = bytes.decode(b'\xF0\x9F\x95\x98', 'utf8')  # часы
        offset = 0
        dict_rus_days = {'Monday': 'понедельник', 'Tuesday': 'вторник', 'Wednesday': 'среда',
                         'Thursday': 'четверг', 'Friday': 'пятница', 'Saturday': 'суббота',
                         'Sunday': 'воскресенье'}

        end_period = count_days
        for shedule in shedule_13_input:
            date_n = datetime.strptime(shedule['datetime'], '%Y-%m-%d')
            if date_n.date() < datetime.now().date():
                offset += 1
                end_period += 1
                continue
            else:
                break

        for shedule in shedule_13_input[offset:end_period]:
            date = datetime.strptime(shedule['datetime'], '%Y-%m-%d')
            date = datetime.strftime(date, '%d/%m/%Y, %A')
            oneday = '{}{}\n\n'.format(emoji1, date)
            dict_shedule = dict()
            for lecture in shedule['discs'][::-1]:
                startDate = dateutil.parser.parse(lecture['startDate']).strftime("%H:%M")
                endDate = dateutil.parser.parse(lecture['endDate']).strftime("%H:%M")
                room = lecture['Room']
                name_lecture = lecture['Disc']
                type_lecture = lecture['Type']
                lecturer = lecture['Lecturer']
                dict_shedule[startDate] = (
                    ' *{}*\n  {}{}-{}\n  _Аудитория_: {}\n  _Тип_: {}\n  _Преподаватель_: {}\n\n'.format(
                        name_lecture,
                        emoji2,
                        startDate,
                        endDate,
                        room,
                        type_lecture,
                        lecturer))
            for key in sorted(list(dict_shedule)):
                oneday += dict_shedule[key]
                # print(startDate,dict_shedule[startDate])
            oneday += " ---------- \n\n"
            oneday = self.find_replace(oneday, dict_rus_days)
            raspisanie.append(oneday)

        date_now = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M')
        # Добавить дату обновления расписания в конце
        # shedule =  'Дата обновления расписания: {}'.format(date_now)
        return raspisanie


def get_dict():
    shed_dict = dict()
    for key in links_dict.keys():
        dict_ = dict()
        for i in range(1, 3):
            print(key, i)
            dict_[i] = Shedule(prof=key, course=i).shedule_day(5)

        shed_dict[key] = dict_

    date_now = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M')
    shed_dict['Дата'] = 'Дата обновления: {}'.format(date_now)
    return shed_dict