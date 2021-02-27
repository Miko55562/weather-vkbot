# -*- coding: utf-8 -*-

import time
import requests
import vk_api
from datetime import datetime
from googletrans import Translator

vk_session = vk_api.VkApi(token='') #токен вк группы

def mane(vk_session):
    from vk_api.longpoll import VkLongPoll, VkEventType
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.from_group:
            print('******** НОВОЕ СООБЩЕНИЕ ********')
            print('Пользователь:', event.user_id, '\nСообщение:', event.text)
            wether('', translator.translate(event.text, dest='en').text, vk, event)
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            event.text = event.text.lower()
            if event.text == "1" or event.text == "москва":
                s = "0"
                city_id = 524901
                city = 'Moskva'
                print('Запрос id Москвы')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '2' or event.text == "санкт петербург" or event.text == "питер":
                s = "0"
                city_id = 498817
                city = 'Saint Petersburg'
                print('Запрос id Санкт-Петербурга')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '3' or event.text == "новосибирск":
                s = "0"
                city_id = 1496747
                city = 'Novosibirsk'
                print('Запрос id Новосибирске')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '4' or event.text == "екатеринбург" or event.text == "екб":
                s = "0"
                city_id = 1486209
                city = 'Ekaterinburg'
                print('Запрос id Екатеринбурге')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '5' or event.text == "нижней новгород":
                s = "0"
                print('id получен')
                city_id = 520555
                city = 'Nizhny Novgorod'
                print('Запрос id Нижнего Новгорода')
                wether(city_id, city, vk, event)
            elif event.text == '6' or event.text == "казань":
                s = "0"
                city_id = 551487
                city = 'Kazan'
                print('Запрос id Казань')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '7' or event.text == "челябинск":
                s = "0"
                city_id = 1508291
                city = 'Chelyabinsk'
                print('Запрос id Челябинска')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '8' or event.text == "омск":
                s = "0"
                city_id = 1496153
                city = 'Omsk'
                print('Запрос id Омска')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '9' or event.text == "самара":
                s = "0"
                city_id = 499099
                city = 'Samara'
                print('Запрос id Самары')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '10' or event.text == "ростов на дону":
                s = "0"
                city_id = 501175
                city = 'Rostov on don'
                print('Запрос id Ростов-на-Дону')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '11' or event.text == "уфа":
                s = "0"
                city_id = 479561
                city = 'Ufa'
                print('Запрос id Уфа')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '12' or event.text == "красноярск":
                s = "0"
                city_id = 1502026
                city = 'Krasnoyarsk'
                print('Запрос id Красноярск')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '13' or event.text == "пермь":
                s = "0"
                city_id = 511196
                city = 'Perm'
                print('Запрос id Пермь')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '14' or event.text == "воронеж":
                s = "0"
                city_id = 472045
                city = 'Voronezh'
                print('Запрос id Воронеж')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '15' or event.text == "волгоград":
                s = "0"
                city_id = 472757
                city = 'Volgograd'
                print('Запрос id Волгоград')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '16' or event.text == "сызрань":
                s = "0"
                city_id = 484972
                city = 'Syzran'
                print('Запрос id Сызрань')
                print('id получен')
                wether(city_id, city, vk, event)

            else:
                print('******** НОВОЕ СООБЩЕНИЕ ********')
                print('Пользователь:',event.user_id,'\nСообщение:', event.text)
                wether('',translator.translate(event.text, dest='en').text,vk, event)


def wether(city_id, city, vk, event):
    access_key = "3c32677556a6389d7599087ae1cac74a"
    params = {
        'access_key': access_key,
        'query': city
    }
    try:
        res = requests.get('http://api.weatherstack.com/current', params)
        data = res.json()
        print(data)
        data= data.get('current')
        print(data.get('weather_descriptions'))
        if data.get('weather_descriptions') == ['Clear']: # солнечно
            emoji = "&#9728;"
        elif data.get('weather_descriptions') == ["rain"] or data.get('weather_descriptions') == ["heavy rain"]: # дождик
            emoji = "&#127783;"
        elif data.get('weather_descriptions') == ['Smoke']: # дымка
            emoji = "&#127787;"
        elif data.get('weather_descriptions') == ['Overcast'] or data.get('weather_descriptions') == ['Partly cloudy']: # облачно
            emoji = "&#9925;"
        elif data.get('weather_descriptions') == ['Light Snow'] or data.get('weather_descriptions') == ['Light Snow Shower'] or data.get('weather_descriptions') == ['Heavy Snow Shower']: # слабый снегопад
            emoji = "&#127784;"
        elif data.get('weather_descriptions') == ['Heavy Snow, Blowing Snow'] or data.get('weather_descriptions') == ['Blowing Snow'] or data.get('weather_descriptions') == ['Heavy snow']: # сильный снегопад метель
            emoji = "	&#127788;"
        elif data.get('weather_descriptions') == "thunderstorm": # гроза
            emoji = "&#9928;"
        elif data.get('weather_descriptions') == "thunderstorm": # гроза
            emoji = "&#9928;"
        else:
            emoji = "&#127744;"

        weather_descriptions = str(", ".join(data.get('weather_descriptions')))
        weather_descriptions = translator.translate(weather_descriptions, src='en', dest='ru').text
        if weather_descriptions == 'Прозрачный': weather_descriptions = 'ясно'
        elif weather_descriptions == 'Дым': weather_descriptions='дымка'
        city = translator.translate(city, src='en', dest='ru').text
        city = 'Город: ' + city + ' 🏙\n'
        weather_descriptions = 'Погода: ' + weather_descriptions.lower() + ' ' + emoji + "\n"
        temperatur = 'Температура: '+str(data.get('temperature'))+"°C 	&#127777;\n"
        feelslike = "По ощущению: "+str(data.get('feelslike'))+"°C 	&#127777;\n"
        if data.get('wind_dir')=='N': wind_dir = 'северный'
        elif data.get('wind_dir')=='S': wind_dir = 'южный'
        elif data.get('wind_dir')=='E': wind_dir = 'восточный'
        elif data.get('wind_dir')=='W': wind_dir = 'западный'
        elif data.get('wind_dir')=='NE': wind_dir = 'северо-восточный'
        elif data.get('wind_dir') == 'NNE': wind_dir = 'северо-северо-восточный'
        elif data.get('wind_dir') == 'NW': wind_dir = 'северо-западный'
        elif data.get('wind_dir') == 'NNW': wind_dir = 'северо-северо-западный'
        elif data.get('wind_dir') == 'SE': wind_dir = 'юго-восточный'
        elif data.get('wind_dir') == 'SSE': wind_dir = 'юго-юго-восточный'
        elif data.get('wind_dir') == 'SW': wind_dir = 'юго-западный'
        elif data.get('wind_dir') == 'SSW': wind_dir = 'юго-юго-западный'
        elif data.get('wind_dir') == 'WNW': wind_dir = 'западный-северо-западный'
        elif data.get('wind_dir') == 'ENE': wind_dir = 'восточный-северо-восточный'
        elif data.get('wind_dir') == 'WSW': wind_dir = 'западный-юго-западный'
        elif data.get('wind_dir') == 'ESE': wind_dir = 'юго-юго-западный'
        wind_speed = "Ветер: "+ wind_dir + ', ' + str(round(data.get('wind_speed')/3.6,2))+ " м/с 💨\n"
        cloudcover = "Влажность: "+str(data.get('humidity'))+"% 	&#128167;\n"
        visibility = "Видемость: "+str(data.get("visibility"))+"км 🔭\n"
        humidity = "Облачность: "+str(data.get("humidity"))+"% ☁\n"

        print(weather_descriptions)
        vk.messages.send(user_id=event.user_id,
                         message=city + weather_descriptions + temperatur + feelslike + wind_speed + cloudcover + visibility + humidity,
                         random_id='0')
    except:
        if event.from_user:  # Если написали в ЛС
            vk.messages.send(user_id=event.user_id,
                             message='Не удалось определить город 😒',
                             random_id='0')
        elif event.from_chat:  # Если написали в Беседе
            vk.messages.send(  # Отправляем собщение
                chat_id=event.chat_id,
                message='Не удалось определить город 😒',
                random_id='0')

translator = Translator()
mane(vk_session)
