# -*- coding: utf-8 -*-

import time
import vk_api
import requests
from datetime import datetime
from google_trans_new import google_translator
from vk_api.longpoll import VkLongPoll, VkEventType

# токен вк группы


def mane():
    try:
        print('Started')
        vk_session = vk_api.VkApi(
        token='')
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        print('Подключились)')
        for event in longpoll.listen():
            if event.from_group:
                print('******** СООБЩЕНИЕ В ЧАТЕ *******')
                print(datetime.now())
                print('Пользователь:', event.user_id, '\nСообщение:', event.text)
                wether(translator.translate(event.text, lang_tgt='en'), vk, event)
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                event.text = event.text.lower()
                print('******** НОВОЕ СООБЩЕНИЕ ********')
                print(datetime.now())
                print('Пользователь:', event.user_id, '\nСообщение:', event.text)
                if event.text == "1" or event.text == "москва":
                    # city_id = 524901
                    city = 'Moskva'
                    wether(city, vk, event)
                elif event.text == '2' or event.text == "санкт петербург" or event.text == "питер":
                    # city_id = 498817
                    city = 'Saint Petersburg'
                    wether(city, vk, event)
                elif event.text == '3' or event.text == "новосибирск":
                    # city_id = 1496747
                    city = 'Novosibirsk'
                    wether(city, vk, event)
                elif event.text == '4' or event.text == "екатеринбург" or event.text == "екб":
                    # city_id = 1486209
                    city = 'Ekaterinburg'
                    wether(city, vk, event)
                elif event.text == '5' or event.text == "нижней новгород":
                    # city_id = 520555
                    city = 'Nizhny Novgorod'
                    wether(city, vk, event)
                elif event.text == '6' or event.text == "казань":
                    # city_id = 551487
                    city = 'Kazan'
                    wether(city, vk, event)
                elif event.text == '7' or event.text == "челябинск":
                    # city_id = 1508291
                    city = 'Chelyabinsk'
                    wether(city, vk, event)
                elif event.text == '8' or event.text == "омск":
                    # city_id = 1496153
                    city = 'Omsk'
                    wether(city, vk, event)
                elif event.text == '9' or event.text == "самара":
                    # city_id = 499099
                    city = 'Samara'
                    wether(city, vk, event)
                elif event.text == '10' or event.text == "ростов на дону":
                    # city_id = 501175
                    city = 'Rostov on don'
                    wether(city, vk, event)
                elif event.text == '11' or event.text == "уфа":
                    # city_id = 479561
                    city = 'Ufa'
                    wether(city, vk, event)
                elif event.text == '12' or event.text == "красноярск":
                    # city_id = 1502026
                    city = 'Krasnoyarsk'
                    wether(city, vk, event)
                elif event.text == '13' or event.text == "пермь":
                    # city_id = 511196
                    city = 'Perm'
                    wether(city, vk, event)
                elif event.text == '14' or event.text == "воронеж":
                    # city_id = 472045
                    city = 'Voronezh'
                    wether(city, vk, event)
                elif event.text == '15' or event.text == "волгоград":
                    # city_id = 472757
                    city = 'Volgograd'
                    wether(city, vk, event)
                elif event.text == '16' or event.text == "сызрань":
                    # city_id = 484972
                    city = 'Syzran'
                    wether(city, vk, event)
                elif event.text == '16' or event.text == "прага":
                    city = 'Prague'
                    wether(city, vk, event)

                else:
                    print('******** НОВОЕ СООБЩЕНИЕ ********')
                    print('Пользователь:', event.user_id, '\nСообщение:', event.text)
                    wether(translator.translate(event.text, lang_tgt='en'), vk, event)
    except requests.exception.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(3)
        
    except vk_api.exceptions.ApiError:
        print('Ошибка авторизации: недопустимый токен авторизации\nХотить переподключиться? (да или нет)')
        while True:
            if input().lower() == 'да':
                mane()
            elif input().lower() == 'нет':
                break
            else:
                print('Да или Нет?')


def wether(city, vk, event):
    access_key = ""
    params = {
        'access_key': access_key,
        'query': city
    }
    try:
        res = requests.get('http://api.weatherstack.com/current', params)
        data = res.json()
        print(data)
        data = data.get('current')
        sunylist = [['Clear'], ['Sunny']]
        rainlist = [["Heavy rain"], ["Rain"], ['Patchy rain possible']]
        smokelist = [['Smoke']]
        overcastlist = [['Partly cloudy'], ['Overcast'], ['Cloudy']]
        lightsnowlist = [['Light Rain And Snow'], ['Light Snow'], ['Light Snow Shower'], ['Snow']]
        hardsnowlist = [['Heavy Snow Shower'], ['Heavy Snow, Blowing Snow'], ['Blowing Snow'], ['Heavy snow']]
        thunderstormlist = [['Thunderstorm'], ['Storm'], ['Hurricane'], ['Tempest']]
        if sunylist.count(data.get('weather_descriptions')) != 0:  # солнечно
            emoji = "☀"
        elif rainlist.count(data.get('weather_descriptions')) != 0:    # дождик
            emoji = "🌧"
        elif smokelist.count(data.get('weather_descriptions')) != 0:    # дымка
            emoji = "🌫"
        elif overcastlist.count(data.get('weather_descriptions')) != 0:   # облачно
            emoji = "⛅"
        elif lightsnowlist.count(data.get('weather_descriptions')) != 0:  # слабый снегопад
            emoji = "🌨"
        elif hardsnowlist.count(data.get('weather_descriptions')) != 0:   # сильный снегопад метель
            emoji = "🌬"
        elif thunderstormlist.count(data.get('weather_descriptions')) != 0:    # гроза
            emoji = "⛈"
        else:
            emoji = "🌀"

        weather_descriptions = str(", ".join(data.get('weather_descriptions')))
        weather_descriptions = translator.translate(weather_descriptions, lang_src='en', lang_tgt='ru')
        if weather_descriptions == 'Прозрачный':
            weather_descriptions = 'ясно'
        elif weather_descriptions == 'Дым':
            weather_descriptions = 'дымка'
        city = translator.translate(city, lang_src='en', lang_tgt='ru')
        city = 'Город: ' + city + ' 🏙\n'
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

        vk.messages.send(
            user_id=event.user_id,
            message=city + weather_descriptions + temp + feelslike + wind + cloud + vis + humidity,
            random_id='0')
        print('Ответ отправлен \n'+city + weather_descriptions +
                     temp + feelslike + wind + cloud + vis + humidity)
        print('******** СООБЩЕНИЕ ЗАКРЫТО ********')

    except AttributeError:
        print('Город '+event.text+"  не найден(")
        if event.from_user:  # Если написали в ЛС
            vk.messages.send(
                user_id=event.user_id,
                message='Не удалось определить город 😒',
                random_id='0')
        elif event.from_chat:  # Если написали в Беседе
            vk.messages.send(  # Отправляем собщение
                chat_id=event.chat_id,
                message='Не удалось определить город 😒',
                random_id='0')

if __name__ == '__main__':
    translator = google_translator()
    print('Подключаемся')
    mane()
