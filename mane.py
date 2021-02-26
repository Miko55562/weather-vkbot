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
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == 'Погода' or event.text == 'Второй вариант фразы':  # Если написали заданную фразу
                print('******** НОВОЕ СООБЩЕНИЕ ********')
                print('Пользователь:', event.user_id, '\nСообщение:', event.text)
            if event.text == "1":
                s = "0"
                city_id = 524901
                city = 'Moskva'
                print('Запрос id Москвы')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '2':
                s = "0"
                city_id = 498817
                city = 'Saint Petersburg'
                print('Запрос id Санкт-Петербурга')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '3':
                s = "0"
                city_id = 1496747
                city = 'Novosibirsk'
                print('Запрос id Новосибирске')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '4':
                s = "0"
                city_id = 1486209
                city = 'Ekaterinburg'
                print('Запрос id Екатеринбурге')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '5':
                s = "0"
                print('id получен')
                city_id = 520555
                city = 'Nizhny Novgorod'
                print('Запрос id Нижнего Новгорода')
                wether(city_id, city, vk, event)
            elif event.text == '6':
                s = "0"
                city_id = 551487
                city = 'Kazan'
                print('Запрос id Казань')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '7':
                s = "0"
                city_id = 1508291
                city = 'Chelyabinsk'
                print('Запрос id Челябинска')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '8':
                s = "0"
                city_id = 1496153
                city = 'Omsk'
                print('Запрос id Омска')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '9':
                s = "0"
                city_id = 499099
                city = 'Samara'
                print('Запрос id Самары')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '10':
                s = "0"
                city_id = 501175
                city = 'Rostov on don'
                print('Запрос id Ростов-на-Дону')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '11':
                s = "0"
                city_id = 479561
                city = 'Ufa'
                print('Запрос id Уфа')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '12':
                s = "0"
                city_id = 1502026
                city = 'Krasnoyarsk'
                print('Запрос id Красноярск')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '13':
                s = "0"
                city_id = 511196
                city = 'Perm'
                print('Запрос id Пермь')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '14':
                s = "0"
                city_id = 472045
                city = 'Voronezh'
                print('Запрос id Воронеж')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '15':
                s = "0"
                city_id = 472757
                city = 'Volgograd'
                print('Запрос id Волгоград')
                print('id получен')
                wether(city_id, city, vk, event)
            elif event.text == '16':
                s = "0"
                city_id = 484972
                city = 'Syzran'
                print('Запрос id Сызрань')
                print('id получен')
                wether(city_id, city, vk, event)

            else:
                print('******** НОВОЕ СООБЩЕНИЕ ********')
                print('Пользователь:',event.user_id,'\nСообщение:',event.text)
                if event.from_user:  # Если написали в ЛС
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message='''
                        Выберете город:
                        1. Москва
                        2. Санкт-Петербург
                        3. Новосибирск
                        4. Екатеринбург
                        5. Нижней Новгород
                        6. Казань
                        7. Челябинск
                        8. Омск
                        9. Самара
                        10. Ростов-на-Дону
                        11. Уфа
                        12. Красноярск
                        13. Пермь
                        14. Воронеж
                        15. Волгоград
                        16. Сызрань
                        ''',
                        random_id='0')
def wether(city_id, city, vk, event):
    access_key = "3c32677556a6389d7599087ae1cac74a"
    weather_descriptions = ''
    params = {
        'access_key': access_key,
        'query': city
    }
    if city_id != 0:
        res = requests.get('http://api.weatherstack.com/current', params)
        data = res.json()
        print(data)
        data= data.get('current')
        print(data.get('weather_descriptions'))
        if data.get('weather_descriptions') == ['Clear']: # солнечно
            weather_descriptions = "ясно"
            emoji = "&#9728;"
        elif data.get('weather_descriptions') == ["rain"] or data.get('weather_descriptions') == ["heavy rain"]: # дождик
            weather_descriptions = "дождь"
            emoji = "&#127783;"
        elif data.get('weather_descriptions') == "fog" or data.get('weather_descriptions') == "haze" or data.get('weather_descriptions') == "dull": # дымка
            weather_descriptions = "дымка"
            emoji = "&#9729;"
        elif data.get('weather_descriptions') == ['Overcast'] or ['Partly cloudy']: # облачно
            emoji = "&#9925;"
            weather_descriptions = "пасмурно"
        elif data.get('weather_descriptions') == ['Light Snow Shower']: # гроза
            emoji = "&#9928;"
            weather_descriptions = "гроза"
        elif data.get('weather_descriptions') == "thunderstorm": # гроза
            emoji = "&#9928;"
            weather_descriptions = "гроза"
        elif data.get('weather_descriptions') == "thunderstorm": # гроза
            emoji = "&#9928;"
            weather_descriptions = "гроза"
        elif data.get('weather_descriptions') == "thunderstorm": # гроза
            emoji = "&#9928;"
            weather_descriptions = "гроза"
        else:
            weather_descriptions = 'неизвестно'
            emoji = "&#127744;"

        weather_descriptions = str(", ".join(data.get('weather_descriptions')))
        weather_descriptions = translator.translate(weather_descriptions, src='en', dest='ru').text
        if weather_descriptions == 'Прозрачный': weather_descriptions = 'ясно'
        elif weather_descriptions == 'Дым': weather_descriptions='дымка'
        city = translator.translate(city, src='en', dest='ru').text
        city = 'Город: ' + city + '\n'
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
        elif data.get('wind_dir') == 'SE': wind_dir = 'юга-васточный'
        elif data.get('wind_dir') == 'SSE': wind_dir = 'юга-юга-восточный'
        elif data.get('wind_dir') == 'SW': wind_dir = 'юга-западный'
        elif data.get('wind_dir') == 'SSW': wind_dir = 'юга-юга-западный'
        wind_speed = "Ветер: "+ wind_dir + ', ' + str(data.get('wind_speed'))+ "м/с\n"
        cloudcover = "Влажность: "+str(data.get('cloudcover'))+"% 	&#128167;\n"
        visibility = "Видемость: "+str(data.get("visibility"))+"км\n"

        print(weather_descriptions)
        vk.messages.send(user_id=event.user_id,
                         message=city + weather_descriptions + temperatur + feelslike + wind_speed + cloudcover + visibility,
                         random_id='0')
        city_id = 0

translator = Translator()
mane(vk_session)
