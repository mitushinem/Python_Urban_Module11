import requests
from requests import RequestException

from config import url, headers

import numpy as np
import pandas as pd


def get_request(url, headers, param):
    try:
        response = requests.get(url, headers=headers, params=param)
        if response.status_code:
            return response.json()
        else:
            response.raise_for_status()
    except RequestException as err:
        print(err)


def realtime_weather(param):
    data = get_request(url=url, headers=headers, param=param)
    return (f'name: {data["location"]["name"]}, '
            f'tz_id: {data["location"]["tz_id"]}, '
            f'temperature: {data["current"]["temp_c"]}')




def func_np():
    a = np.array([1, 2, 3])
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

    print(a)
    print(a2)
    print(a3)
    c = np.array([1, 2, 3], dtype='float32')
    print(c)
    a = np.zeros((2, 2), dtype='int32')
    print(a)

    b = np.ones((4, 2, 2), dtype='int32')
    print(b)

    c = np.full((2, 2), 5)
    print(c)

    d = np.random.rand(3, 2)
    print(d)

    e = np.random.randint(-5, 10, size=(4, 4))
    print(e)


def func_np2():
    a = np.array([1, 2, 3, 4])
    print(a + 3)
    print(a - 2)
    print(a * 2)
    print(a / 2)
    print(a ** 2)



def func_pd1():

    city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
            'Год основания': [1147, 1703, 1893, 1723],
            'Население': [11.9, 4.9, 1.5, 1.4]}  # Создаём словарь с нужной информацией о городах.

    df = pd.DataFrame(city)  # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.

    return df  # Выводим DataFrame на экран.


if __name__ == '__main__':
    state = ['Paris', 'Minsk', 'Smolensk', 'Moscow']

    for state in state:
        print(realtime_weather({"q": state}))

    func_np()
    func_np2()
    print(func_pd1())