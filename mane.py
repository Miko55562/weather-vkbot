# -*- coding: utf-8 -*-

import os
import sys
import time
import vk_api
import requests
import traceback
from datetime import datetime
from google_trans_new import google_translator
from vk_api.longpoll import VkLongPoll, VkEventType


def mane(apikey, adminid, weatherkey):
    try:
        vk_session = vk_api.VkApi(
        token=apikey)
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        sendmessage(adminid, vk, 'Бот онлайн 🤙')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                firstnamecase = vk.users.get(user_id=event.user_id)[0]['first_name'] + ' '
                lastnamecase = vk.users.get(user_id=event.user_id)[0]['last_name']
                ans = '******** НОВОЕ СООБЩЕНИЕ ********\n'
                ans += str(datetime.now())[:-10]
                ans += '\nПользователь: '
                ans += str(firstnamecase) + str(lastnamecase)
                ans += '\nid: ' + str(event.user_id) + '\nСообщение: ' + event.text
                sendmessage(adminid, vk, message=ans)
                event.text = event.text.lower()
                if event.text == "начать":
                    sendmessage(event.user_id, vk, 'Доброго времени суток ' + str(firstnamecase) + ' 😏')
                    sendmessage(event.user_id, vk, 'WeatherBot🤖 поддерживает все города мира 🌍')
                    sendmessage(event.user_id, vk, 'Попробуйте прислать название любого города!')
                elif event.text == "reboot":
                    if event.user_id == int(adminid):
                        sendmessage(adminid, vk, 'Бот будет перезагружен')
                        os.execl(sys.executable, sys.executable, *sys.argv)
                    else:
                        sendmessage(event.user_id, vk, 'У вас недостаточно прав')
                        sendmessage(adminid, vk, 'Пользователь: ' + event.user_id + ' превышение прав!')
                elif event.text == "update":
                    if event.user_id == adminid:
                        sendmessage(adminid, vk, 'Проверка обновлений')
                        os.execl(sys.executable, sys.executable, *sys.argv)
                    else:
                        sendmessage(event.user_id, vk, 'У вас недостаточно прав')
                        sendmessage(adminid, vk, 'Пользователь: ' + event.user_id + ' превышение прав!')
                else:
                    wether(event.text, vk, event)

    except Exception:
        traceback.print_exc()
        excepterror(apikey, adminid, traceback.format_exc())
        time.sleep(3)
        mane(apikey, adminid, weatherkey)


def wether(city, vk, event):
    access_key = weatherkey
    params = {
        'access_key': access_key,
        'query': city
    }
    try:
        res = requests.get('http://api.weatherstack.com/current', params)
        data = res.json()
        data = data.get('current')
        sunylist = [['Clear'], ['Sunny']]
        rainlist = [["Heavy rain"], ["Rain"], ['Patchy rain possible']]
        smokelist = [['Smoke']]
        overcastlist = [['Partly cloudy'], ['Overcast'], ['Cloudy']]
        lightsnowlist = [['Light Rain And Snow'], ['Light Snow'], ['Light Snow Shower'], ['Snow'], ['Light snow showers']]
        hardsnowlist = [['Heavy Snow Shower'], ['Heavy Snow, Blowing Snow'], ['Blowing Snow'], ['Heavy snow']]
        thunderstormlist = [['Thunderstorm'], ['Storm'], ['Hurricane'], ['Tempest']]
        if sunylist.count(data.get('weather_descriptions')) != 0:  # солнечно
            emoji = "☀"
            weather_descriptions = 'солнечно'
        elif rainlist.count(data.get('weather_descriptions')) != 0:    # дождик
            emoji = "🌧"
            weather_descriptions = 'дождик'
        elif smokelist.count(data.get('weather_descriptions')) != 0:    # дымка
            emoji = "🌫"
            weather_descriptions = 'дымка'
        elif overcastlist.count(data.get('weather_descriptions')) != 0:   # облачно
            emoji = "⛅"
            weather_descriptions = 'облачно'
        elif lightsnowlist.count(data.get('weather_descriptions')) != 0:  # слабый снегопад
            emoji = "🌨"
            weather_descriptions = 'слабый снегопад'
        elif hardsnowlist.count(data.get('weather_descriptions')) != 0:   # сильный снегопад метель
            emoji = "🌬"
            weather_descriptions = 'сильный снегопад метель'
        elif thunderstormlist.count(data.get('weather_descriptions')) != 0:    # гроза
            emoji = "⛈"
            weather_descriptions = 'гроза'
        else:
            print(data.get('weather_descriptions'))
            emoji = "🌀"
            weather_descriptions = str(", ".join(data.get('weather_descriptions')))
            weather_descriptions = translator.translate(weather_descriptions, lang_tgt='ru')
        sendmessage(adminid, vk, weather_descriptions)
        if weather_descriptions == 'Прозрачный':
            weather_descriptions = 'ясно'
        elif weather_descriptions == 'Дым':
            weather_descriptions = 'дымка'
        city = 'Город: ' + str(city[0].upper())+city[1:] + ' 🏙\n'
        weather_descriptions = 'Погода: ' + weather_descriptions.lower() + ' ' + emoji + "\n"
        temp = 'Температура: '+str(data.get('temperature'))+"°C 🌡\n"
        feelslike = "По ощущению: "+str(data.get('feelslike'))+"°C 🌡\n"
        wind_dir = ''
        if data.get('wind_dir') == 'N':
            wind_dir = 'северный'
        elif data.get('wind_dir') == 'S':
            wind_dir = 'южный'
        elif data.get('wind_dir') == 'E':
            wind_dir = 'восточный'
        elif data.get('wind_dir') == 'W':
            wind_dir = 'западный'
        elif data.get('wind_dir') == 'NE':
            wind_dir = 'северо-восточный'
        elif data.get('wind_dir') == 'NNE':
            wind_dir = 'северо-северо-восточный'
        elif data.get('wind_dir') == 'NW':
            wind_dir = 'северо-западный'
        elif data.get('wind_dir') == 'NNW':
            wind_dir = 'северо-северо-западный'
        elif data.get('wind_dir') == 'SE':
            wind_dir = 'юго-восточный'
        elif data.get('wind_dir') == 'SSE':
            wind_dir = 'юго-юго-восточный'
        elif data.get('wind_dir') == 'SW':
            wind_dir = 'юго-западный'
        elif data.get('wind_dir') == 'SSW':
            wind_dir = 'юго-юго-западный'
        elif data.get('wind_dir') == 'WNW':
            wind_dir = 'западный-северо-западный'
        elif data.get('wind_dir') == 'ENE':
            wind_dir = 'восточный-северо-восточный'
        elif data.get('wind_dir') == 'WSW':
            wind_dir = 'западный-юго-западный'
        elif data.get('wind_dir') == 'ESE':
            wind_dir = 'юго-юго-западный'
        wind = "Ветер: " + wind_dir + ', ' + str(round(data.get('wind_speed')/3.6, 2)) + " м/с 💨\n"
        cloud = "Влажность: "+str(data.get('humidity'))+"% 💧\n"
        vis = "Видемость: "+str(data.get("visibility"))+"км 🔭\n"
        humidity = "Облачность: "+str(data.get("humidity"))+"% ☁"

        sendmessage(adminid, vk, 'Ответ отправлен \n'+city + weather_descriptions +
                         temp + feelslike + wind + cloud + vis + humidity + '\n******** СООБЩЕНИЕ ЗАКРЫТО ********')
        sendmessage(event.user_id, vk, city + weather_descriptions + temp + feelslike + wind + cloud + vis + humidity)

    except AttributeError:
        sendmessage(adminid, vk, 'Город ' + city + ' не найден!')
        if event.from_user:  # Если написали в ЛС
            sendmessage(event.user_id, vk, 'Не удалось определить город 🤪')
        elif event.from_chat:  # Если написали в Беседе
            sendmessage(event.chat_id, vk, 'Не удалось определить город 🤪')


def sendmessage(user, vk, message):
    vk.messages.send(user_id=user, message=message, random_id='0')

def excepterror(apikey, adminid, tracebackerror):
    vk_session = vk_api.VkApi(
    token=apikey)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    vk.messages.send(user_id=adminid, message=tracebackerror, random_id='0')

if __name__ == '__main__':
    apikey = open('apikey.txt', 'r').readline()
    adminid = open('adminid.txt', 'r').readline()
    weatherkey = open('weatherkey.txt', 'r').readline()
    translator = google_translator()
    mane(apikey, adminid, weatherkey)
